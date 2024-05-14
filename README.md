<p align="center"><img width=100% src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/156c2a82-1471-48af-ace8-afea4190df0e"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
# AlgoEase Server
## Overview
Algorithmic trading, the use of computer programs to execute trades based on pre-defined rules, offers several advantages over manual trading, including speed, efficiency, and emotional detachment. However, the technical expertise needed to design and implement trading algorithms can be a barrier for many potential users. This project aims to address this challenge by creating a user-friendly system that allows individuals to express their trading ideas in plain language, without requiring extensive coding knowledge.

## Features

- **Natural Language Strategy Submission:** Users can input trading strategies using plain language, describing conditions, parameters, and desired outcomes without requiring coding knowledge.
- **Advanced NLP Interpretation:** Utilize advanced natural language processing techniques to accurately analyze user-submitted strategies, extracting key elements like buy/sell signals, entry/exit points, and risk management parameters.
- **Model Creation:** Automatically translate interpreted strategies into a structured model suitable for algorithmic execution, capturing the core logic of the user's idea.
- **Deployment and Monitoring:** Enable deployment of successful strategies in live trading environments, with automated execution based on predefined rules. 

## Screenshots

<p align="center">
  <img src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/a467272e-8410-41da-a72d-d3ee2246c7e7" width="24%" />
  <img src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/9714d067-22e2-472d-9beb-580d5e8464d9" width="24%" />
  <img src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/8a76c19d-7244-47ac-9e56-809907c7e7ee" width="24%" />
 <img src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/b1bf6100-6b17-4d75-a293-91ef9aba1884" width="24%" />
</p>

## Getting Started

### Prerequisites

To run the algo-ease-server, you'll need:
- Python (version v3.12 or higher) installed on your system.

### Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/afluxmhd/algo-ease-server.git
```

2. Navigate to the project directory:

```bash
cd algo-ease-server
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Open the project in your preferred  IDE or editor.
5. Create a new file named .env inside the source folder.
6. Add the following code to the .env file
```bash
GOOGLE_API_KEY='YOUR_API_KEY'
```
8. Run the server on your  device :
   
```bash
Python -m uvicorn app.api:app --reload
```

## Authors

<a href="https://github.com/afluxmhd/algo-ease-server/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=afluxmhd/algo-ease-server" />
</a>
