## 安装YouCompleteMe的步骤

0. 用vundle中的安装太慢,所以自己手动安装

1. 安装插件管理工具
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```
  在.vimrc中插件管理处加入:
```
Plugin 'Valloric/YouCompleteMe'
```

2. 安装ycm
```
cd .vim/bundle
git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe
git submodule update--init--recursive
./install.py --clang-completer
```

3. 在.vimrc中添加下列
```
let g:ycm_global_ycm_extra_conf = ‘~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py’ 
```
