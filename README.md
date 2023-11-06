# django-production-guide
<hr>

### Step by Step guide to deploy django application.
<hr>

<!-- Project Structure Start -->
<details> 
<summary>Project Structure</summary>

```
.
├── manage.py
├── README.md
├── requirements
├── simple_medium_clone
```

1) `simple_medium_clone` is our main django application.
2) `requirements` dir contains diffrent requirement for diff environments.

#### Inside requirements

```requirements
.
├── base.txt
├── local.txt
└── production.txt
```
base.txt will contains common dependencies

#### How to use dependency inheritance
Inside requirement file use <i>-r filename</i> to include all dependencies of <i>filename</i> into file.

```
-r base.txt
```

#### Create gitignore file
```npx gitignore python```
This will generate .gitignore file for Python projects 
OR we can add this when creating project repo.
</details> 
<!-- Project Structure End -->