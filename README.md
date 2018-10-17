nolecture
---

- This is a proof of concept for composing content of different types, all
  in Jupyter notebooks (see `content/` directories), into a single shareable
  Jupyter notebook for usage in workshops
 
### The Problem

I run workshops in Python at the University of Pittsburgh. I first attempted to
do this in a traditional lecture based workshop, however I had complaints that
the workshop:

- was too easy
- was too difficult
- didn't include information on:
    - data science libraries (e.g. pandas)
    - machine learning (e.g. scikit-learn)
    - deep learning (e.g. tensorflow)
    - databases (e.g. dataset)
    - linear algebra (e.g. numpy and scipy)
    - web scraping (e.g. requests and beautifulsoup)
- didn't provide examples in _insert domain here_

### How To Handle These Issues?

First, I am not an expert in pedagogy but I plan on consulting with folks
who are. I have gone through a few iterations of this workshop and I am quite
happy with the content.

In Undergrad, I took Chemistry I/II where the Professor used [Process Oriented
Guided Inquiry Learning POGIL](https://www.pogil.org/). If I wanted to boil
down POGIL into a few sentences (poor representation, but sufficient for this
discussion):

```
Students are given notebooks to work on with a group during class.
These notebooks present fundamental concepts in the domain with questions to
reinforce those concepts.
```

I used this idea and applied it to scientists learning programming. The
backgrounds scientists have in programming vary wildly. I have encountered
undergraduates, graduate students, postdoctoral associates, and professors.
There is a POGIL for Computer Science undergraduates, but this just doens't
work for scientists. Scientists look at programming similarly to a spreadsheet,
programming is a tool which helps them complete cool new science. It needs
to be presented as a tool, not an academic discipline.

Using a Jupyter Notebook with a guided learning approach I can:

- target beginners and advanced students
- students can work at their own pace
- students can attend the workshop multiple times and learn new things
- students can use their notebook as a reference tool
- create a solid base of understanding to move forward into Python libraries

A __very__ important note, when teaching using this style you need to engage
early and often! I talk more during this guided approach than I did lecturing.
Many students will not ask you questions until you walk up to them and ask them
how they are doing. The students will be enthusiastic if you are as well.

### Building a Notebook

The `nolecture.py` tool simply concatenates content written in Jupyter
Notebooks into a single Notebook which you can share with your students. I
originally worked on [tapestry](https://github.com/barrymoo/tapestry) which was
a single notebook, but I found iterations on the notebooks difficult.
Additionally tapestry was broken up into beginner, intermediate, and advanced
notebooks but I wanted all users to see the same content. Advanced users will
just progress more rapidly. The separation allows the content creator to focus
on single concepts at a time and make sure it is self-contained. Notebooks
should not depend on cells ran from other notebooks. It is fine to include
reminders about concepts they would have previously gained. Jupyter Notebooks
are JSON and therefore I decided to define concatenatations as JSON.  Example
(from `notebooks/functions.json`):

```json
{
    "content": [
        {
            "functions": [
                "intro",
                "members",
                "anonymous"
            ]
        }
    ]
}
```

The `content` section contains a list of dictionaries. In this case we define one
dictionary with the key `functions` whose value is a list of `["intro",
"members", "anonymous"]`. This will concatenate the files
`content/functions/intro.ipynb`, `content/functions/members.ipynb`, and
`content/functions/anonymous.ipynb` inside the template `skel.jinja2`. I used
jinja because I was familiar with it from using Flask. I would like to
use templates more for things like contact information, etc. You would run
`nolecture.py` in the following way:

```python
./nolecture.py notebooks/functions.json > Functions.ipynb
```

My current workshop notebook is built with `notebooks/beginner.json`.

### What's Next

- The content uses very basic data science examples
    - Domain specific variations will be important!
    - My current idea is to have graduate students in a domain specialize
      notebooks into specific branches
- There is specific information related to how my users connect to JupyerHub
    - And my contact information
        - This would benefit from templating
- Think about fundamental pedagogy of programming to scientists
- I expect you to be running your own JupyterHub, this might not be very convenient
    - BinderHub could be useful here
- Many users also ask for R programming workshops, I need someone to convert the
  code into R
- Only enough material for a relatively short workshop
    - Mine are usually 3 hours, beginners will not finish in 3 hours
- Adding library specific notebooks for students who have the base knowledge, current plans:
    - pandas (somewhat together from tapestry)
    - scikit-learn and tensorflow
    - dataset
    - numpy and scipy
    - requests and beautifulsoup
- Dealing with data dependencies, e.g. those in `data/`
