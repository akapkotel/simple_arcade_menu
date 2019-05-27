This is a simple in-game menu-builder for Arcade games made in Python. It requires Python3.6 and Arcade2.0.8. Menus are
basically a bunch of classes defining how Arcade should display clickable elements and what functions to call when they
are activated.

To make it work you must import it: at least Cursor, Menu and Button classes in your game script. You do not even need
to make your own implementations of methods.

SharedVariable:
This class makes it possible to share a common value between many objects in the game and update them dynamically. Just
assign the SharedVariable instance as variable value.

Menu:
Menu class to work requires you to pass into it's constructor a single SubMenu object, which would be the main menu of
your menu-system displayed first when player enters menu (e.g. starts the game). For Menu to work it is also required
that a Cursor object is initialized - but SubMenu requires it too.

SubMenu:
SubMenu class to work requires only a list of MenuElement objects (eg. Button), Cursor object initialised in your game,
and a hook to your arcade.Window object. It's up to you how would you manage the menu in your game, but you can easily
do that with a single bool variable checked in on_update() method to decide if you want to draw your game or call the
draw() method of Menu instance.

Cursor:
Cursor class to work requires only being initialised by your arcade.Window instance and kept as it's attribute to easily
call it's methods: on_update() and on_draw(), when you want Cursor object to being used.

MenuElement:
MenuElement class (and all deriving from it, eg, Button) requires only being initialised with whatever functions passed
to them as callbacks and after you create your Buttons, remember of passing them as a list to the Menu instance. Some
classes deriving from MenuElement (e.g. Slider) requires SharedVariable objects to be passed as argument.

So, the order of imports, instantiating classes and handling them in your game should be:
1. SharedVariable - which is the class you need to assign it's instances as the values for all attributes and other
variables you need to be changed with usage of Slider and RadioButton elements of the Menu
2. Cursor class object and implement arcade methods: on_mouse_motion(), on_mouse_press(), on_mouse_drag() and
on_mouse_release() to call the Cursor methods instead.
3. List of MenuElement objects (e.g. Button) - with at least one element.
4. (Optional) arcade.Texture object as background for menu
5. At least one SubMenu class object with List from (3) passed as menu_elements argument, and (optional) texture from
(4) passed as background argument.
6. Menu class object with SubMenu from (5) passed as main_menu argument.
7. Adding Cursor on_update() and Menu update() methods calls to the on_update() method in your game.
8. Adding Cursor draw() and Menu draw() methods calls to the on_draw() method in your game.
9. Logic determining if Menu and Cursor should be updated and drawn in current frame are up to you.

9. If you need multi-level menu, you must instantiate some SubMenu objects with their own lists of MenuElements and set
the callbacks to toggle_submenu() method of your Menu with the 'name' of your SubMenu as argument.

IMPORTANT: app_hook attribute of Menu and Cursor must be the same arcade.Window object!

Licensing:
For license look at the LICENSE file.
