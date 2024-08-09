from glob import glob
from os.path import join
from subprocess import check_call

class TestAnsibleLint(object):

    def test_ansible_lint_parent(self):
        command = ' '.join([
            'ansible-lint',
            '-c /home/runner/.ansible-lint.cfg',
            '--fix',
            '/home/runner/ansible',
        ])
        try:
            result = check_call(command, shell=True)
        except Exception:
            result = 1
        assert 0 == result
