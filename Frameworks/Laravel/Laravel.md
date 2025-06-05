#framework 

A [[MVC]] framework written in [[PHP]]

 **Laravel**

[Install Tailwind CSS with Laravel](https://tailwindcss.com/docs/guides/laravel)
[Fireship - Laravel in 100 Seconds](https://www.youtube.com/watch?v=rIfdg_Ot-LI)
  
## Model, View, Controller, Route locations

**Models**
- Project → http → models

**Views**
- Project → resources → views

**Controllers**
- Project → app → http → controllers

**Routes**
- located in web.php
## Security

Use @csrf ([[CSRF]]) when doing stuff with a post route (i.e. register)
## [[Artisan]] creation commands

**Model**

php artisan make:model [NAME]