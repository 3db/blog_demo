wget "https://github.com/3db/blog_demo/releases/download/1.0/studioX_Stage.blend.zip"
unzip studioX_Stage.blend.zip
mkdir data/texture_swaps/blender_environments/
mv studioX_Stage.blend data/texture_swaps/blender_environments/
rm studioX_Stage.blend.zip
rm -rf __MACOSX
