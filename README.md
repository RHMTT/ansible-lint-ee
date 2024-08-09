This repo has the builder files needed to create an ansible-lint container. You can use this from your desktop or within a pipeline to run ansible-lint scans at scale.

I created this to be used solely for the FQCN updates and deprecated items.

Intructions.

git clone this repo
ensure ansible-builder is installed
within this directory run

ansible-builder build -v 3 -t lint-ee

To execute this use the following:

podman run --privileged -v ~/ansible/Development/Linting/ansible-lamp-stack-playbook:/home/runner/ansible  -v ~/.ansible/collections/ansible_collections:/home/runner/ansible/.ansible/collections/ansible_collections --userns keep-id --workdir=/home/runner/ansible localhost/lint-ee pytest /home/runner/scripts/lint.py



