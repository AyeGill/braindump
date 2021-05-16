#! /usr/bin/env python3
import glob
from pathlib import Path

def escstring(string):
    return string.replace("$","$$").replace(" ","$ ").replace(":","$:")
files_root = glob.glob("/home/eigil/Dropbox/org/*.org")
files_nroot = glob.glob("/home/eigil/Dropbox/org/*/*.org", recursive=True)

files = files_root + files_nroot
for f in files:
    if f.find(":") != -1:
        print(f, "contains :")

# Colon files cause issues with relref. Ignore them for now
files = list(filter(lambda x: x.find(":") == -1, files))


# We make the blog posts file later...
files.remove("/home/eigil/Dropbox/org/pages/20200414104653-blog_posts.org")

with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l ~/.emacs.d/init.el --eval \"(ayegill/braindump-file \\"`echo $in`\\")"
  description = org2md $in

rule mkdummyblog
    command = echo \"Dummy file...\" > $out
    description = mk dummy blog posts
""")
    
    for f in files:
        path = Path(f)
        output_file = f"content/posts/{escstring(path.with_suffix('.md').name)}"
        ninja_file.write(f"""
build {output_file}: org2md {escstring(str(path))}
""")

    ninja_file.write(f"""
build content/posts/20200414104653-blog_posts.md : mkdummyblog
""")
import subprocess
#subprocess.call(["ninja"])
