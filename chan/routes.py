from chan import app, db, ALLOWED_EXTENSIONS, secure_filename, os
from chan.models import Board, Thread, Replies
from chan.forms import RepliesForm, ThreadForm
from flask import render_template, redirect, url_for, flash, request
import datetime, random


@app.route("/")
def home_page():
    boards = Board.query.all()

    return render_template("home.html", boards=boards)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/<board>/", methods=["POST", "GET"])
def board_page(board):
    form = ThreadForm()
    board_selected = Board.query.filter_by(board_short_name=board).first()
    threads = Thread.query.filter_by(board=board_selected.id)
    replies = Replies.query
    datetime_now = datetime.datetime.now()
    newfilename = ""

    if form.validate_on_submit() and request.method == "POST":
        if "image_file" in request.files:
            print("image_file")
            file = request.files["image_file"]
            if file and allowed_file(file.filename):
                print("file good")
                filename = secure_filename(file.filename)
                newfilename = (
                    str(random.randint(10000000, 100000000))
                    + "."
                    + filename.rsplit(".", 1)[1].lower()
                )
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], newfilename))

        thread_create = Thread(
            name_check=form.name.data,
            datetime=datetime_now,
            board=board_selected.id,
            text=form.text.data,
            image_file=newfilename,
        )

        db.session.add(thread_create)
        db.session.commit()

        flash(
            f"Congratulations! You created a thread",
            category="success",
        )

        return redirect(f"/{board}/")

    return render_template(
        "board.html",
        board=board_selected,
        threads=threads,
        thread_form=form,
        replies=replies,
    )


@app.route("/<board>/<thread>", methods=["POST", "GET"])
def thread_page(board, thread):
    form = RepliesForm()

    board_selected = Board.query.filter_by(board_short_name=board).first()
    thread_selected = Thread.query.filter_by(id=thread).first()
    replies = Replies.query.filter_by(thread=thread_selected.id)

    datetime_now = datetime.datetime.now()
    newfilename = ""

    if form.validate_on_submit() and request.method == "POST":
        if "image_file" in request.files:
            print("image_file")
            file = request.files["image_file"]
            if file and allowed_file(file.filename):
                print("file good")
                filename = secure_filename(file.filename)
                newfilename = (
                    str(random.randint(10000000, 100000000))
                    + "."
                    + filename.rsplit(".", 1)[1].lower()
                )
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], newfilename))

        create_replies = Replies(
            name_check=form.name.data,
            datetime=datetime_now,
            text=form.text.data,
            image_file=newfilename,
            thread=thread_selected.id,
        )

        db.session.add(create_replies)
        db.session.commit()

        flash(
            f"Congratulations! You created a thread",
            category="success",
        )

        return redirect(f"/{board}/{thread}")

    return render_template(
        "thread.html",
        thread=thread_selected,
        board=board_selected,
        replies_form=form,
        replies=replies,
    )
