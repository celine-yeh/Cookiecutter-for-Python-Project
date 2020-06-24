# Cookiecutter for Python Project

以往在建置專案時，會要重新 setup 許多東西，其中也包括了目錄文件架構、文件內容、ignore 檔、lint 檔等等，但每次在開發專案時都要重複這樣的動作**非常耗時且容易出錯**，因此 Cookiecutter 的出現解決了這項問題，讓使用者可以下**一個 command 完成所有建置步驟**。

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) 就像是快速做餅乾的工具，而 templates 是餅乾的模型，Cookiecutter 依照這個 templates 做出來的餅乾都會是一樣的，唯一的差異在於每個專案可以有自己的變數，例如：專案名稱、路徑等，都透過 Jinja2 來替換這些變數。

> `100% of templating is done with Jinja2. This includes file and directory names.`
> 
> ⎯⎯ [Cookiecutter Features](https://cookiecutter.readthedocs.io/en/latest/readme.html?highlight=jinja2#features)

另外，templates 並**不局限於任何程式語言**，也可以在同一個專案下使用多種語言。

## Quickstart

```
$ cookiecutter git@github.com:celine-yeh/Cookiecutter-for-Python-Project.git
$ cd project
$ git init
$ git remote add origin git@github.com...
$ git add .
$ git commit -m "Basic architecture"
$ git push -u origin master
```
