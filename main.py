import praw
import prawcore
import config



# Allow access to the bot

reddit = praw.Reddit(client_id="CLIENTID",
                    client_secret="CLIENTSECRET",
                    password="PASSWORD",
                    username="USERNAME",
                    user_agent="Flair-based removal bot")

subreddit = reddit.subreddit("subname")

print('Starting Flair-Comment Bot')



def flair_mod_stream(reddit, iteration=1):
    print('flair mod stream started')

    try:
        subreddit = reddit.subreddit("confidentlyincorrect")

        for flair_edit in subreddit.mod.stream.log(action='editflair', skip_existing=True):
            check_flair = True
            print("Working")

            # skip non-submission flair edits
            if not flair_edit.target_fullname.startswith('t3_'):
                check_flair = False
                print("Working for non-submission")

            if check_flair:
                flair_edit_submission = reddit.submission(flair_edit.target_fullname.lstrip('t3_'))
                

                if hasattr(flair_edit_submission, 'link_flair_template_id'):
                    flair_id = flair_edit_submission.link_flair_template_id
                    remove = False
                    print("post removed")

                    if flair_id == '6949363a-af40-11eb-954f-0e3381d474c5':
                        # rule 1: all posts must be on topic
                        remove = True
                        removal_reason = ('''Hello! Thank you for submitting to /r/confidentlyincorrect, however, your submission has been removed for the following violating one or more of our rule(s):

- **[Rule 2: ](https://www.reddit.com/r/confidentlyincorrect/about/rules/) All Posts must be on topic!**

This sub is designed around arrogant people, sure of their abilities, getting their dreams crushed instantly. Your submission didn't quite fit that model and it is for that reason that it got removed.

Please [contact the mods](https://www.reddit.com/message/compose?to=%2Fr%2Fconfidentlyincorrect) if you feel this was wrong.

^Beep ^Boop. ^I ^am ^a ^bot, ^any ^chat ^requests ^and ^pms ^go ^into ^an ^unmonitered ^inbox. ^Contact ^the ^mods ^instead!''')
                    if flair_id == '0875eb44-af42-11eb-88f6-0ec2f09a1c3f':
                        # rule 2: =dont be an ass
                        remove = True
                        removal_reason = ('''Hello! Thank you for submitting to /r/confidentlyincorrect, however, your submission has been removed for violating one or more of our rule(s):

- **[Rule 3: ](https://www.reddit.com/r/confidentlyincorrect/about/rules/) Don't be an ass!**

Let's not bully like it's middle school. Don't be an ass to people.

Please [contact the mods](https://www.reddit.com/message/compose?to=%2Fr%2Fconfidentlyincorrect) if you feel this was wrong.

^Beep ^Boop. ^I ^am ^a ^bot, ^all ^chat ^requests ^and ^pms ^go ^into ^an ^unmonitered ^inbox. ^Contact ^the ^mods ^instead!''')
                    if flair_id == '78bc2d64-af42-11eb-9e9a-0eb7e3e5aa53':
                        # rule 4: Don't get TOO Political
                        remove = True
                        removal_reason = ('''Hello! Thank you for submitting to /r/confidentlyincorrect, however, your submission has been removed for violating one or more of our rule(s):

- **[Rule 4: ](https://www.reddit.com/r/confidentlyincorrect/about/rules/) Don't get TOO political!**

Making a quick joke about the person in a video or gif is fine. completely being an ass and going on with your political opinions is not fine. No matter what they are.

Please [contact the mods](https://www.reddit.com/message/compose?to=%2Fr%2Fconfidentlyincorrect) if you feel this was wrong.

^Beep ^Boop. ^I ^am ^a ^bot, ^all ^chat ^requests ^and ^pms ^go ^into ^an ^unmonitered ^inbox. ^Contact ^the ^mods ^instead!''')
                    if flair_id == 'd90f5614-af42-11eb-9b93-0ec4747bf55d':
                        # rule 5: nothing scripted
                        remove = True
                        removal_reason = ('''Hello! Thank you for submitting to /r/confidentlyincorrect, however, your submission has been removed for violating one or more of our rule(s):

- **[Rule 5: ](https://www.reddit.com/r/confidentlyincorrect/about/rules/) Nothing scripted!**

Whatever you posted was from a TV Show or youtube skit, or something like that. It was scripted, and not genuine, which means we can't really have it on the sub. Sorry.

Please [contact the mods](https://www.reddit.com/message/compose?to=%2Fr%2Fconfidentlyincorrect) if you feel this was wrong.

^Beep ^Boop. ^I ^am ^a ^bot, ^all ^chat ^requests ^and ^pms ^go ^into ^an ^unmonitered ^inbox. ^Contact ^the ^mods ^instead!''')
                    if flair_id == '66c2338c-af43-11eb-b591-0eec2cafde45':
                        # rule 6: Really, seriously, don’t be a cunt
                        remove = True
                        removal_reason = ('''Hello! Thank you for submitting to /r/confidentlyincorrect, however, your submission has been removed for violating one or more of our rule(s):

- **[Rule 6: ](https://www.reddit.com/r/confidentlyincorrect/about/rules/) No reposts!**

On this subreddit, we don't like seeing the same confidently incorrect posts again and again. As we have seen your post before on this subreddit, it has been removed

Please [contact the mods](https://www.reddit.com/message/compose?to=%2Fr%2Fconfidentlyincorrect) if you feel this was wrong.

^Beep ^Boop. ^I ^am ^a ^bot, ^all ^chat ^requests ^and ^pms ^go ^into ^an ^unmonitered ^inbox. ^Contact ^the ^mods ^instead!''')
                  
                    if remove:

                        # remove the submission and leave a comment
                        removal_comment = flair_edit_submission.reply(removal_reason)

                        removal_comment.mod.distinguish(how='yes', sticky=True)
                        removal_comment.mod.lock()

                        flair_edit_submission.mod.remove()
                        flair_edit_submission.mod.lock()

                        print(f'submission by u/{flair_edit_submission.author} removed by u/{flair_edit._mod} via flair.')

                       
            else:
                print('flair_edit response skipped')

    except prawcore.exceptions.ServerError as error:
        print(f'skipping flair_edit due to PRAW error: {type(error)}: {error}')

    except prawcore.exceptions.ResponseException as error:
        print(f'skipping flair_edit due to PRAW error: {type(error)}: {error}')
    except Exception as e:
        print(e)
    iteration += 1

    if iteration <= 10:
        flair_mod_stream(reddit, iteration)

    else:
        print('killing flair mod stream, >10 skipped logs')

flair_mod_stream(reddit)
