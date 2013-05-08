sublimetext-commitment
======================

Sublime Text adoption of the great [Commitment](https://github.com/ngerakines/commitment) project.

* **OS X**: Hit `Command+Shift+L`,`Command+Shift+O`,`Command+Shift+L`
* **Linux** / **Windows**: Hit `Ctrl+Shift+L`,`Ctrl+Shift+O`,`Ctrl+Shift+L`

for *a quick laugh*.

*Visit [http://whatthecommit.com/](http://whatthecommit.com/) for the web version.*

Usage
-----
* Type `What the commit` in the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows).
* **OS X**: Hit `Command+Shift+L`,`Command+Shift+O`,`Command+Shift+L`.
* **Linux** / **Windows**: Hit `Ctrl+Shift+L`,`Ctrl+Shift+O`,`Ctrl+Shift+L`.

You will see a random commit message printed to the status bar. The commit message is also added to your clipboard, so paste away.
Define your own shortcuts through `Preferences > Package Settings > Commitment`.

Permalinks to the [web version](http://whatthecommit.com/) are printed to the console (`View > Show Console`) for you to share with your nerdy friends.
```
Commitment:
(\ /)
(O.o)
(> <) Bunny approves these changes.
Permalink: http://whatthecommit.com/0e0c1a4060a298158f3c4ef526f03f86
```

Installation
------------

### Using [Package Control](http://wbond.net/sublime_packages/package_control):

* Click on **Preferences > Package Settings > Package Control > Settings - User**.
* Edit and add the following key/value-pairs to that **json** file:

```js
{   
    "package_name_map": {
        "sublimetext-commitment": "Commitment"
    },
    "repositories": [
        "https://github.com/janraasch/sublimetext-commitment"
    ]
}
```

* Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows).
* Select `Package Control: Install Package`.
* Select `Commitment` to install.


### Not using Package Control:
   * Save files to the `Packages/Commitment` directory, then relaunch Sublime:
      * Linux: `~/.config/sublime-text-2/Packages/Commitment`
      * Mac: `~/Library/Application Support/Sublime Text 2/Packages/Commitment`
      * Windows: `%APPDATA%/Sublime Text 2/Packages/Commitment`

License
---------
Copyright (c) 2013 Jan Raasch

This project and its contents are open source under the MIT license.
