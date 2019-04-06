from flask import Flask, request, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
jinja_env = jinja2.environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = flask(__name__)
app.config['debug'] = True