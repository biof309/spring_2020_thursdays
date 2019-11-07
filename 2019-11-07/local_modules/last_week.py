#!/usr/bin/env python

def generate_test_tree(test_dir,overwrite=False):
    seasons = 'spring summer autumn winter'.split()
    animals = 'cat dog bat monkey elephant'.split()

    if test_dir.exists() and overwrite:
        shutil.rmtree(test_dir)
    for animal,season in itertools.product(animals,seasons):
        this_loop_dir = test_dir / animal / season
        text_path = this_loop_dir / 'data.txt'
        text_path.parent.mkdir(parents=True)
        text_string = generate_text()
        text_path.write_text(text_string)