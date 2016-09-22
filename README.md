Role Name
=========

basically an ansible implementation of [Mathias Bynens'](https://github.com/mathiasbynens) [.osx](https://mths.be/osx) with
some omissions (that will maybe get implemented eventually) and some additions.

Requirements
------------

Ruby

Role Variables
--------------

i don't want to spend the time to copy *all* the variables over here
(there's a lot), so check out `defaults/main.yml`... it lays out all the
variables, their defaults, and which tasks file they are used in.

nothing should happen when you include the role without defining any
`osx_*` variables. you can copy the contents of `defaults/main.yml` into
your role statement (or somewhere else you get your vars from) and define
or switch to `on` the vars you want.

vars that trigger one way behaviors (set something in a state and make sure
it stays that way) are `on` / `off` values, where `off` does nothing and
`on` sets the state. turning these back to `off` *does not* undo the changes.

variables that can be used to set values are commented out in
`defaults/main.yml` with examples and type info.

Dependencies
------------

-   [nrser.state_mate](https://github.com/nrser/ansible-nrser.state_mate)
-   [nrser.rb](https://github.com/nrser/ansible-nrser.rb)

Example Playbook
----------------

```yaml
---
- name: neil's osx

  hosts: all

  roles:

  - role: nrser.osx
    # i hate the ui sounds
    osx_disable_ui_sounds:                                    on
    
    # i like the scroll bars to always be shown
    osx_always_show_scroll_bars:                              on
    
    # etc...
```

License
-------

BSD

Author Information
------------------

<https://github.com/nrser>
