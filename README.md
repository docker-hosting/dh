## Docker hosting CLI
If you installed *docker hosting* as [described above](#installation) there's a `dh` command to administrate your websites.

### dh create
With `dh create` you can create a new website.
````bash
Usage:
    dh create <template_name> <website_name>

Arguments:
    <template_name>   One of the template repositories on the docker hosting
                      github account, but without the -template suffix.
    <website_name>    The name of the website.
````

The example above would be `dh create wordpress my-blog.com`.

### dh cd `TODO`
With `dh cd` you can jump into a websites directory.
````bash
Usage:
    dh cd <website_name>

Arguments:
    <website_name>    The name of the website
````

### dh backup `TODO`
With `dh backup` you can backup one ore more websites.
````bash
Usage:
    dh backup [options] <website_name>

Arguments:
    <website_name>    The name of the website

Options:
    -a, --all         Backup all websites. The <website_name> argument will be ignored.
    --website-only    Backup only the website(s) without the container data. All the
                      files inside the websites directory will be backed up but without
                      calling the backup script(s).
````

### dh restore `TODO`
With `dh restore` you can restore one ore more websites.
````bash
Usage:
    dh restore [options] <website_name>

Arguments:
    <website_name>    The name of the website

Options:
    -a, --all         Restore all websites. The <website_name> argument will be ignored.
    --website-only    Restore only the website(s) without the container data. All the
                      files inside the websites directory will be restored but without
                      calling the restore script(s).
````

## Building and running the docker-hosting cli as docker image
```bash
docker build -t dh .

# Now run dh, mount ./webserver to containers /var/www directory
docker run --rm -ti --volume $PWD/webserver:/var/www dh create wordpress test.de
```
