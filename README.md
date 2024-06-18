# iNetStorm: Python Network Testing Tool for Unified DoS Testing.

Command Line python script top perfom a variety of networking tests
It aims to unify DoS test behind a simple script (In version 2 maybe a GUI), abstracting much of the backend work to enable developers to focus on other things.
**Warning:** This script is published for educational purposes only! Author will accept no responsibility for any consequences, damage or loss which might result from use.

iNetStorm is a Python script designed to perform a wide range of networking tests, with a focus on unifying Denial of Service (DoS) testing through a simple command. This powerful tool enables comprehensive evaluations of network resilience and security.

Key features of iNetStorm:

Unified DoS testing: iNetStorm streamlines the DoS testing process by integrating various methods and attacks into a single tool.
Control and precision: Configure and customize test parameters such as attack intensity, duration, and target, allowing for precise and controlled testing.
Realistic simulation: iNetStorm realistically emulates attacks, enabling the evaluation of network and system resilience under adverse conditions.
Intuitive interface: iNetStorm provides an easy-to-use command-line interface for quick test initiation, termination, and parameter customization.
Detailed reports: Generate comprehensive reports with statistics and relevant metrics, enabling in-depth analysis of network response to different attack types.
iNetStorm is an ideal tool for assessing network security and conducting controlled resilience tests. Strengthen your system against DoS attacks by identifying potential vulnerabilities using iNetStorm's precise and comprehensive testing capabilities.

## Table of Contents.

- [Feature Highlights](#feature-highlights)
- [Getting Started](#getting-started)
- [Made with](#made-with)
- [Terminology](#terminology)
- [Developer Guide](#developer-guide)

## Feature Highlights.

- Easily integrate custom tools to unify operations behind a **single script**
- Use attacks like UDP flood, Ping of death, Post petting with fake data and much more.

## Getting Started 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

### Pre-requisitos 📋

_What things you need to install the software and how to install them_

Clone the repository.

```
mkdir python_network_tests
cd python_network_tests
git clone https://github.com/GerardoBZentenoM/DoS-BruteForce-FakeData.git
cd DoS-BruteForce-FakeData
```

Download a Virtual Env. (in Ubuntu 20)

```
sudo apt install python3-venv
```

Create a virtual env (in Ubuntu 20)

```
python3 -m venv .venv
```

Activate the venv (in Ubuntu 20)

```
source .venv/bin/activate
```

Need sudo permition

### Instalación 🔧

_A series of step-by-step examples that tell you what to run to get a development environment up and running._

_Clone the repository._

Download the requeriments

```
pip install -r requeriments.txt
```

_Run:_ (in Ubuntu 20)

```
sudo ./.venv/bin/python3 main.py
```

Example:

![alt text](/sources/pythonetwork-test.png)

## Made with 🛠️

- [Python](https://www.python.org/) - As programming language.
- [Scapy](https://scapy.net/) - A powerful interactive packet manipulation program - License GPL v2.

## Wiki 📖

You can find out much more about how to use this project in our [Wiki](https://github.com/tu/proyecto/wiki)

## Authors ✒️

- **Gerardo Zenteno** - _Developer_ - [GitHub](https://github.com/GerardoBZentenoM)

you can also view the list of all [contributors](https://github.com/your/project/contributors)

---

⌨️ Made with ❤️ by [Gerardo Zenteno](https://www.linkedin.com/in/brallan-zenteno/) 😇

Feel free to colaborate <3
