# HBCU Rate My Professor API

A REST API that allows HBCU students to rate and review professors based on factors that actually matter to them such as teaching pace, late work policy, assignment frequency, and more

Built with **FastAPI**, **SQLAlchemy**, and **SQLite**

## Live Demo
Base URL: https://hbcu-rate-my-professor.onrender.com

Interactive Docs: https://hbcu-rate-my-professor.onrender.com/docs

## The Problem
Rate My Professor exists but doesn't serve HBCU students well. 
This API is built specifically for that community with rating 
categories that reflect what HBCU students actually care about.

## Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | /professors | List all professors |
| GET | /professors/{name} | Get one professor |
| GET | /professors/{name}/reviews | Get reviews for a professor |
| POST | /reviews | Submit a review |
| POST | /professors/{name}/bookmark | Bookmark a professor |
| GET | /bookmarks | View all bookmarks |

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Deployed on Render

## Author
Built by Samuel Bissou — Comp Sci @ Huston-Tillotson University