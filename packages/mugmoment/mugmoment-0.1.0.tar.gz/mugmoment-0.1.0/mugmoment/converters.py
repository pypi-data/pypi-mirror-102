def ttv_raw_to_simple_format(raw_comments):
    comments = []
    include_hours = raw_comments[-1]["content_offset_seconds"] >= 3600
    for comment in raw_comments:
        simple_data = {
            "author": comment["commenter"]["display_name"],
            "body": comment["message"]["body"],
            "offset": comment["content_offset_seconds"],
            "fancy_offset": _offset_to_fancy_timestamp(
                comment["content_offset_seconds"], include_hours
            ),
        }
        comments.append(simple_data)
    return comments


def ttv_raw_to_txt(raw_comments):
    simple_comments = ttv_raw_to_simple_format(raw_comments)
    comments = []
    for comment in simple_comments:
        text_data = f"{comment['fancy_offset']} <{comment['author']}> {comment['body']}"
        comments.append(text_data)
    return "\r\n".join(comments)


def _offset_to_fancy_timestamp(offset, include_hours=True):
    # Convert offset to int to drop the msecs
    offset = int(offset)

    # Derive hours, minutes and seconds
    hours = int(offset / 3600) if include_hours else 0
    minutes = int((offset - (hours * 3600)) / 60)
    seconds = offset - ((hours * 3600) + (minutes * 60))

    fancy_timestamp = f"{minutes:02d}:{seconds:02d}"
    if include_hours:
        fancy_timestamp = f"{hours:02d}:" + fancy_timestamp

    return fancy_timestamp


def ttv_raw_to_html(raw_comments):
    comments = []
    include_hours = raw_comments[-1]["content_offset_seconds"] >= 3600
    for comment in raw_comments:
        timestamp = _offset_to_fancy_timestamp(
            comment["content_offset_seconds"], include_hours
        )
        color = comment["message"].get("user_color", "#000000")
        name = comment["commenter"]["display_name"]

        html_data = f'<span class="timeoffset">{timestamp}</span> '
        html_data += f'<span class="author" style="color: {color}">{name}</span>: '
        html_data += '<span class="message">'

        for fragment in comment["message"]["fragments"]:
            if "emoticon" in fragment:
                emote_id = fragment["emoticon"]["emoticon_id"]
                html_data += f'<img alt="{fragment["text"]}" class="emote emote-{emote_id}" src="https://static-cdn.jtvnw.net/emoticons/v2/{emote_id}/default/dark/1.0" srcset="https://static-cdn.jtvnw.net/emoticons/v2/{emote_id}/default/dark/1.0 1x,https://static-cdn.jtvnw.net/emoticons/v2/{emote_id}/default/dark/2.0 2x,https://static-cdn.jtvnw.net/emoticons/v2/{emote_id}/default/dark/3.0 4x">'
            else:
                html_data += fragment["text"]

        html_data += "</span>"

        comments.append(html_data)
    return "<br>\r\n".join(comments)
