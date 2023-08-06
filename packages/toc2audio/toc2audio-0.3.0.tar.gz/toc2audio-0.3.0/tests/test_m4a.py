#!/usr/bin/env python3

import unittest
import pathlib
import tempfile
import shutil

import mutagen
import mutagen.mp4

import toc2audio


class m4a(unittest.TestCase):
    def setUp(self):
        self.tmp_dir_obj = tempfile.TemporaryDirectory()
        self.tmp_dir = pathlib.Path(self.tmp_dir_obj.name)
        self.tmp_file = self.tmp_dir / 'test.m4a'
        shutil.copyfile('silence.m4a', self.tmp_file)

    def tearDown(self):
        self.tmp_dir_obj.cleanup()

    def test_chapters(self):
        md = 'Title\n\n[00:10] First\n\n[00:40] Second'
        toc = toc2audio.Toc(md)
        toc2audio.add_tags_mp4(self.tmp_file, toc, add_chapters=True)
        mp4 = mutagen.mp4.MP4(self.tmp_file)
        self.assertEqual(mp4.tags['\xa9nam'], ['Title'])

        self.assertEqual(len(mp4.chapters), 2)

        for i, v in enumerate(((10, 40, 'First'), (40, 86440, 'Second'))):
            start_time, end_time, title = v
            chap = mp4.chapters[i]
            self.assertEqual(chap.start, start_time)
            self.assertEqual(chap.title, title)

    def test_previous_chapters(self):
        md = 'Title\n\n[00:10] First\n\n[00:40] Second'
        toc = toc2audio.Toc(md)
        toc2audio.add_tags_mp4(self.tmp_file, toc, add_chapters=True)

        md = 'Title 2\n\n[00:23] Third'
        toc = toc2audio.Toc(md)
        toc2audio.add_tags_mp4(self.tmp_file, toc, add_chapters=True)

        mp4 = mutagen.mp4.MP4(self.tmp_file)
        self.assertEqual(mp4.tags['\xa9nam'][0], 'Title 2')
        self.assertEqual(len(mp4.chapters), 1)
        self.assertEqual(mp4.chapters[0].start, 23)
        self.assertEqual(mp4.chapters[0].title, 'Third')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(m4a))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
