# Tachyon

I have been (mis)using tools like Jenkins and like to run Ansible over two years now,
combined with some clever Jenkins DSL and a few hacks it works relay well for our use case.
Still, it's a little weird hybrid so this is a try to solve it.

## The concept behind this

* I expect Ansible to be run often (like once a hour) to validate the environments state.
* Secure, as secure as possible consider that Ansible needs a awful lot of access.
* Easy to read output, highlight errors and changes.

## Setup dev enviroment

You need python, pip and virtualenv. Just type `make` to lauch a dev env.
