#!/bin/sh
OUTFILE=dist/gamefaqs.txt

cat \
  src/introduction.md \
  src/overworld.md \
  src/metaverse.md \
  dist/walkthrough.md \
  dist/ace-walkthrough.md \
  src/confidants.md \
  src/achievements.md \
> $OUTFILE

# GameFAQs Required
sed -i '1s/^/;format:gf-markup\n/' $OUTFILE

# Bold
sed -i "s/\*\*/''/g" $OUTFILE

# Horizontal Rule
sed -i 's/^---/%/' $OUTFILE

# Section Header
sed -i '/^##### /s/$/=====/' $OUTFILE
sed -i '/^#### /s/$/====/' $OUTFILE
sed -i '/^### /s/$/===/' $OUTFILE
sed -i '/^## /s/$/==/' $OUTFILE
sed -i 's/^##### /=====/' $OUTFILE
sed -i 's/^#### /====/' $OUTFILE
sed -i 's/^### /===/' $OUTFILE
sed -i 's/^## /==/' $OUTFILE

# Unordered List
sed -i 's/^        \*/***/' $OUTFILE
sed -i 's/^    \*/**/' $OUTFILE

# Ordered List
sed -i 's/^        [0-9]\+./###/' $OUTFILE
sed -i 's/^    [0-9]\+./##/' $OUTFILE
sed -i 's/^[0-9]\+./#/' $OUTFILE

# Table Header
tac $OUTFILE | sed '/^| --- |/{n; s/| /|*/g}' | tac > dist/temp.txt
mv dist/temp.txt $OUTFILE
sed -i '/^| --- |/d' $OUTFILE
