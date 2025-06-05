**Node Package Manager**

A library and registry for [[JavaScript]] software packages.

---

[YT - What is NPM, and why do we need it?](https://www.youtube.com/watch?v=P3aKRdUyr0s&list=WL&index=46&t=6s)

will be installed along with [[Node.js]]

allows you to install remote packages to use in your own code

A library and registry for [[JavaScript]] software packages.




npm install express
will install locally unlike python whivh is global and you have to use .venv.

to instal globally use the npm -g flag






commands


npm init - Will create file but will ask you questions

npm init -y -// create a package.json file with default settings



npm list // show all packages needed (including dev & project depenencies)
npm list --depth=0 // set custom depth so you don't see what verything else is dependant upon

// Installs locally (relative to the project under node_modules) which is where all package info is stored
npm install [whatever] 


can instally locally or globally
typescript is installed globally for example


in npm install is run in a folder that has a package file then all dependencies will be installed as well



if package lock json file exists it will install the exact major.minor.patch version




```
git rm -r --cached node_modules
git rm -r --cached coverage // Jest

npm install // install all dependencies, dev packages and other packages
```





// Install a package
npm i <packageName>
// Install a specific version of a package
npm i <packageName>@<version>
// Install a package as a development dependency
npm i <packageName> —save-dev
// Uninstall a package
npm un <packageName>
// List installed packages
npm list —depth=0
// View outdated packages
npm outdated
// Update packages
npm update 



nodemon
- watches files and auto reloads them so you dont have to keep re running 