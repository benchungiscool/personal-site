# This site now uses github actions for deployments!!

A big part of my role in DevOps is creating and maintaining CI/CD pipelines with tools like jenkins and gh-actions.

I wanted to experiment with this myself and create a pipeline for changes to the main branch of the repo of this site, as part of my ongoing commitment to spend more time on backend than frontend.

To this end, I created a simple CD script using github actions, which pulls down my latest changes and then redeploy my docker containers for the site itself, and my nginx. This means that I don't have to ssh into my server to make changes to this site, and can test updates to the site on my local before pushing.

