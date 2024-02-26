# Contributing to Resume-Matcher on GitHub

Thank you for taking the time to contribute to [Resume-Matcher](https://github.com/iamsamkhan/ATS-AI-resume-automation.git).

We want you to have a great experience making your first contribution.

This contribution could be anything from a small fix to a typo in our
documentation or a full feature.

Tell us what you enjoy working on and we would love to help!

If you would like to contribute, but don't know where to start, check the
issues that are labeled
`good first issue`
or
`help wanted`.

Contributions make the open-source community a fantastic place to learn, inspire, and create. Any contributions you make are greatly appreciated.

The development branch is `main`. This is the branch where all pull requests should be made.

## Reporting Bugs

Please try to create bug reports that are:

- Reproducible. Include steps to reproduce the problem.
- Specific. Include as much detail as possible: which version, what environment, etc.
- Unique. Do not duplicate existing opened issues.
- Scoped to a Single Bug. One bug per report.

## Testing

Please test your changes before submitting the PR.

## Good First Issues

We have a list of `help wanted` and `good first issue` that contains small features and bugs with a relatively limited scope. Nevertheless, this is a great place to get started, gain experience, and get familiar with our contribution process.

## Development

Follow these steps to set up the environment and run the application.

## How to install

1. Fork the repository [here](https://github.com/iamsamkhan/ATS-AI-resume-automation/fork).

2. Clone the forked repository.

   ```bash
   git clone https://github.com/iamsamkhan/ATS-AI-resume-automation.git
   cd Resume-Matcher
   ```

3. Create a Python Virtual Environment:

   - Using [virtualenv](https://learnpython.com/blog/how-to-use-virtualenv-python/):

     _Note_: Check how to install virtualenv on your system here [link](https://learnpython.com/blog/how-to-use-virtualenv-python/).

     ```bash
     virtualenv env
     ```

   **OR**

   - Create a Python Virtual Environment:

     ```bash
     python -m venv env
     ```

4. Activate the Virtual Environment.

   - On Windows.

     ```bash
     env\Scripts\activate
     ```

   - On macOS and Linux.

     ```bash
     source env/bin/activate
     ```

    **OPTIONAL (For pyenv users)**

   Run the application with pyenv (Refer to this [article](https://realpython.com/intro-to-pyenv/#installing-pyenv))

   - Build dependencies (on ubuntu)
      ```
      sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python openssl
      ```
      ```

      sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev libncurses-dev

      sudo apt-get install python-tk python3-tk tk-dev

      sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
      
      ```

        - pyenv installer
     ```
        curl https://pyenv.run | bash
     ```
   - Install desired python version
     ```
       pyenv install -v 3.11.0
     ```
     
   - pyenv with virtual enviroment 
     ```
        pyenv virtualenv 3.11.0 venv
     ```
     
   - Activate virtualenv with pyenv
     ```
        pyenv activate venv
     ```

     5. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Prepare Data:

   - Resumes: Place your resumes in PDF format in the `Data/Resumes` folder. Remove any existing contents in this folder.
   - Job Descriptions: Place your job descriptions in PDF format in the `Data/JobDescription` folder. Remove any existing contents in this folder.

7. Parse Resumes to JSON:

   ```python
   python run_first.py
   ```

   8. Run the Application:

   ```python
   streamlit run streamlit_app.py
   ```

**Note**: For local versions, you do not need to run "streamlit_second.py" as it is specifically for deploying to Streamlit servers.

**Additional Note**: The Vector Similarity part is precomputed to optimize performance due to the resource-intensive nature of sentence encoders that require significant GPU and RAM resources. If you are interested in leveraging this feature in a Google Colab environment for free, refer to the upcoming blog (link to be provided) for further guidance.

<br/>

### Docker

1. Build the image and start application

   ```bash
       docker-compose up
   ```

2. Open `localhost:80` on your browser

<br/>

### Running the Web Application

The full stack Next.js (React and FastAPI) web application allows users to interact with the Resume Matcher tool interactively via a web browser.

To run the full stack web application (frontend client and backend api servers), follow the instructions over on the [webapp README](/webapp/README.md) file.

<br/>

### Cohere and Qdrant

1.  Visit [Cohere website registration](https://dashboard.cohere.ai/welcome/register) and create an account.
2.  Go to API keys and copy your cohere api key.
3.  Visit [Qdrant website](https://cloud.qdrant.io/) and create an account.
4.  Get your api key and cluster url.
5.  Go to open dashboard in qdrant and enter your api key **for only the first time**

<img src="Assets/img/quadrant_cloud.png" height="60%" width="60%"/>

6.  Now create a yaml file named config.yml in Scripts/Similarity/ folder.

7.  The format for the conifg file should be as below:
    ```yaml
    cohere:
      api_key: cohere_key
    qdrant:
      api_key: qdrant_api_key
      url: qdrant_cluster_url
    ```
8.  Please replace your values without any quotes.

*Note: Please make sure that Qdrant_client's version is higher than v1.1*

<br/>

## Join Us, Contribute!

Pull Requests & Issues are not just welcomed, they're celebrated! Let's create together.




🔔 Share your thoughts in our [Discussions & Announcements](https://github.com/iamsamkhan/ATS-AI-resume-automation.git/discussions).

🚀 Explore and improve our [Landing Page](https://github.com/iamsamkhan/ATS-AI-resume-automation.git). PRs always welcome!

📚 Contribute to the [Resume Matcher Docs](https://github.com/iamsamkhan/ATS-AI-resume-automation.git-Docs) and help people get started with using the software. 

