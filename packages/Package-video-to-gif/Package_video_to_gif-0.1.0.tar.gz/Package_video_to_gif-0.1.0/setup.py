from setuptools import setup, find_packages

setup(
    name='Package_video_to_gif',
    version='0.1.0',
    packages=find_packages(),
    author="Barbara && Watcherley",
    python_requires=">=3.2",
    url="https://github.com/PLeila/videotogif.git",
    description="Un outil pour convertir des vidéos en fichiers GIF.",
    author_email="pierrebarbara012@gmail.com",
    install_requires=[
        # Ajoutez vos dépendances ici
    ],
    entry_points={
        'console_scripts': [
            'videotogif = videotogif.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        # Ajoutez d'autres classifications appropriées
    ],
)
