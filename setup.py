from setuptools import setup

setup(
    name='lektor-nofollow',
    version='0.1',
    author=u'Kenji Wellman',
    author_email='kenji.wellman@gmail.com',
    license='MIT',
    py_modules=['lektor_nofollow'],
    entry_points={
        'lektor.plugins': [
            'nofollow = lektor_nofollow:NofollowPlugin',
        ]
    }
)
