(.NET, .NET Core, .NET Standard, .NET Framework)

A developer platform owned by Microsoft. Can use multiple languages not just C#

---
## Links
- [Tim Corey YT - Explanation](https://www.youtube.com/watch?v=X75vbT-Yv-c&list=WL&index=29)
- [Tim Corey YT - Confusion](https://www.youtube.com/watch?v=4olO9UjRiww&list=WL&index=29)

[[#Execution flow]]
[[#CLR]]

[[#.Net]]
- [[#.Net Framework]]
- [[#.Net Core]]
- [[#.Net Standard]]
- [[#.Net MAUI]]

[[#Deployment]]

---
## Execution flow
source code
	-> compiler
		-> IL (Intermediate Language)
			-> .NET framework [[#CLR]]  **OR**  .Net Core [[#CLR]] 
				-> Executed by the JIT (Just in time compiler)

---
## CLR
Common Language Runtime
.NET languages ([[C Sharp]], C++, F#, VB all compile into this Intermediate Language)

---
## .Net
- Microsoft have dropped the 'Core' name and is now known as just .Net because it has overtaken the .Net Framework version number
- Even versions of .Net will have LTS (Long term support) & uneven versions will have STS (Short term support)

---
## .Net Framework
- Tied into Windows OS can't work on other platforms
- Has support for old OS's
- Comes with everything included
- Stops at .Net Framework 4.8

---
## .Net Core
- Modern framework  / abstraction layer with more features
- Works on most platforms (Windows, Mac, Linux, Android, iOS etc..)
- Faster, removed some legacy support & bloat, removed things it doesn't really need anymore
- Can add extra functionality with [[NuGet]] Packages (including third-party ones)
- Follows best practices (testing, logging, etc...), compliant with industry standards
- Open source
- Known now as [[#.Net]]

---
## .Net Standard
- A interface layer that allows you to compile into either abstraction layer
- Can compile into other abstraction layers like Xamarin / Mono / Unity etc...

---
## .Net MAUI
**Multi-platform App UI**

- a cross-platform framework for creating native mobile and desktop apps with C# and XAML.
- Can develop apps that can run on Android, iOS, macOS, and Windows from a single shared code-base.

---
## Deployment

``` 
A response from Time Corey on a YT comment

You could clarify in the Readme if you wanted to. It shouldn't bother anyone, especially when you say that it is a stand-alone app. If it does invite questions in the interview, that would be a great opportunity. You could talk about wanting to make it as easy as possible on users, so you included .NET as a part of the application so that it could run on any Windows machine. You could also talk about not wanting to shrink the file to only the parts of .NET that it uses because it was a frequently updated exe as you expand the app and you don't want to debug it each time to be sure nothing was missed from .NET. You could talk about your cost/benefit analysis of your time adding new features vs your time validating the shrinking feature was working properly for each build. These are excellent conversations to have with an interviewer.

Don't forget that you actually want to give an interviewer something to talk about. If there is something obvious that they might want to talk about, you can plan for it and be ready to have a great conversation. If you eliminate all of these that you can find, the conversation can go anywhere and you might not be prepared for every eventuality.
```

Steps
- Right click -> publish
- self-contained -> larger file size
- x64

delete from hardrive for google doc space?

git hub tag

v2.0.0
2.0.0
major.minor.patch

AppName version
PostmanCloneApp v2.0.0


---