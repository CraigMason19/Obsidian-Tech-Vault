An open source [[JavaScript]] runtime, a alternative to [[Node.js]]. 
- Runs [[JavaScript]] and [[TypeScript]] with no additional tools or configuration required.
- Has built in formatter, linter, testing & compiling (make an exe)
- Has a standard library
- Compatable with [[NPM]]
- Security first - disallows operations like read / write / net access automatically

---

[DENO - Website](https://deno.com)




| deno --version                                                     | Checks version number and used to see if it is installed |
| ------------------------------------------------------------------ | -------------------------------------------------------- |
| deno init ***(Project name)***                                     | Create a new project                                     |
| deno fmt ***(Optional: filename)***                                | Formats all files / a specific file                      |
| deno lint ***(Optional: filename)***                               | Lints all files / a specific file                        |
| deno run --allow-net ***(Filename)*** <br>deno -N ***(Filename)*** | Allow net permissions                                    |
| deno task **(Taskname)**<br>deno task run                          | Run a custom [[#Tasks]]                                  |
| deno add ***npm:cowsay***                                          | Add a dependancy                                         |

---

## Tasks

Can make custom tasks to make running code easier.  Allows to set custom flags. I.e. permissions

```
// Add in deno.json 
"tasks": {
	"dev": "deno run --watch main.ts",
	"run": "deno run --allow-read main.ts"
},

In terminal:
	deno task run
```
