[![Netlify Status](https://api.netlify.com/api/v1/badges/d6b49afd-cd07-4714-87d1-bc8e8239068f/deploy-status)](https://app.netlify.com/sites/braindump-jethrokuan/deploys)

# Eigil's Braindump

Adapted from [Jethro's Braindump](https://github.com/jethrokuan/braindump)

This braindump is generated via [ox-hugo][ox-hugo] and uses the
[cortex][cortex] theme.

To use this version of the script, modify `build.py`, pointing it at your folder of org-files.
You also need a export-to-markdown setup in your emacs config. Here is mine:

```elisp
(defun ayegill/braindump-file (file)
  (remove-hook! 'find-file-hook #'+org-roam-open-buffer-maybe-h)
  (with-current-buffer (find-file-noselect file)
  (projectile-mode -1)
  (dtrt-indent-mode -1)
  (let ((org-id-extra-files (find-lisp-find-files org-roam-directory "\.org$"))
        (org-hugo-base-dir "~/projects/braindump"))
    (org-hugo-export-wim-to-md))))
```

## Installation instructions

I use the [Ninja](https://ninja-build.org/ "Ninja") build tool to convert my Org
files into Markdown locally. This is so that only changed Org files get
reprocessed into Markdown files. Ninja spawns many Emacs instances in batch mode
running `ox-hugo`, parallelizing the job of exporting the Org files.

To convert all Org files into Markdown, run:

```bash
./build.py
```
to generate the build instructions.
`build.py` is simple enough to inspect.

Then run `ninja` to run the build.

 Once the Markdown files are generated,
we can use Hugo to generate the website.

Install [hugo][hugo]. E.g., on a Mac with Homebrew:

    $ brew install hugo

Make sure the submodule containing the Hugo theme is installed:

    $ git submodule init
    $ git submodule update

Now run hugo to generate the files (find them in `/public`):

    $ hugo

Or run the following to get an immediately browsable website on localhost:

    $ hugo serve

## Common issues

- If some of your org-files contain colons, hugo will choke on the links. There's no way around this execpt to rename your files. To assist this, `build.py` automatically skips files containing colons, and prints a list of them.
- If some of your files contain org-hugo instructions, it will get confused.
- I've inserted a dummy "Blog Posts" file because I had a file that broke the script a lot

[hugo]: https://gohugo.io/
[ox-hugo]: https://github.com/kaushalmodi/ox-hugo
[cortex]: https://github.com/jethrokuan/cortex
[org]: https://github.com/jethrokuan/braindump/tree/master/org
