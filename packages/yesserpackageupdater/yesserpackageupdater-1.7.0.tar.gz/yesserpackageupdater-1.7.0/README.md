
# PIP Package Updater by yesseruser

This is a simple package updater that updates all outdated packages when run.  
Install by running:

``` sh
python -m pip install yesserpackageupdater
```

in CMD or PowerShell on Windows or

``` sh
python3 -m pip install yesserpackageupdater
```

in Mac/Linux's default terminal.

You can use it by running:  

``` sh
yesserpackageupdater
```

in CMD, PowerShell or your OS' default terminal.

~This package only works on Windows.~  
This package works on any operating system since update 1.1.5

If you're running the package from a python file, please **use a subprocess** instead of importing and calling the `update_packages` function. This is because the package can update itself and it can result in an error because of the code changing.
## What's Changed
* Pip warnings when fetching outdated are now suppressed with -q by @yesseruser in https://github.com/yesseruser/YesserPackageUpdater/pull/40
* Added a help function and called it in update_packages. by @yesseruser in https://github.com/yesseruser/YesserPackageUpdater/pull/42


**Full Changelog**: https://github.com/yesseruser/YesserPackageUpdater/compare/1.6.1...1.7.0
