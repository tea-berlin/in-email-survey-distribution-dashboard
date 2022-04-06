## In email survey distribution dashboard

### Context

The **in-email-survey-distribution-dashboard** repo is part of the in-email-survey-project. It hosts the code of the streamlit dashboard for sending out the surveys.

Survey respondents receive emails via Amazon SES containing HTML formatted survey questions. The answering options are displayed as buttons. Each button links to the website that is to be built collaboratively here in the **In-email Survey Counter** repository. The urls underlying each button do not only open the web page, they also transfer various attributes via the url to identify:
- the question that was asked (in the form of a *question code*),
- the selected answering option (in the form of a number), and
- the unique id of the respondent (in the form of a hashed email address ensuring anonymity)
- unique id of the survey itself

### Function of the dashboard

The dashboard serves as interface for sending out the survey. A later version of the dashboard could contain the analytics as well.

### Mode of collaboration

You cannot push directly to the `main` branch. Please push to the branch of the issue you are working on and create a pull request if you want to merge your changes into `main`.

### Setup

To get started, 

1. clone the repository
2. cd into the root folder of your repository
3. create a virtual environment (if you use venv, do the following; otherwise look up which library you want to use instead to create a virtual environment on your local machine)

```
python3 -m venv venv
```

4. activate your virtual environment (if you use venv, do the following; otherwise look up which library you want to use instead to create a virtual environment on your local machine)

```
source venv/bin/activate
```

5. now that your virtual environment is activated, install the packages from `requirements.txt`

```
pip3 install -r requirements.txt
```

6. rename `.env.example` to `.env`

7. start the streamlit application

```
streamlit run app.py
```

### Resources

- check out [streamlit.io](https://streamlit.io/), it is an amazing library