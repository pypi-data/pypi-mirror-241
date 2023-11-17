import json


def convert_openai_messages(messages, function_calling=True):
    new_messages = []

    for message in messages:
        new_message = {"role": message["role"], "content": ""}

        if "message" in message and "image" not in message:
            new_message["content"] = message["message"]

        if "code" in message:
            if function_calling:
                new_message["function_call"] = {
                    "name": "execute",
                    "arguments": json.dumps(
                        {"language": message["language"], "code": message["code"]}
                    ),
                    "parsed_arguments": {
                        "language": message["language"],
                        "code": message["code"],
                    },
                }
            else:
                new_message["content"] += f"\n\n```{message['language']}\n{message['code']}\n```"
                new_message["content"] = new_message["content"].strip()

        new_messages.append(new_message)

        if "output" in message:
            if function_calling:
                new_messages.append(
                    {
                        "role": "function",
                        "name": "execute",
                        "content": message["output"],
                    }
                )
            else:
                if message["output"] == "No output":
                    content = "The code above was executed on my machine. It produced no output. Was that expected?"
                else:
                    content = (
                            "Code output: "
                            + message["output"]
                            + "\n\nWhat does this output mean / what's next (if anything)?"
                    )

                new_messages.append({"role": "user", "content": content})

        if "image" in message:
            image_message = {
                "role": "user" if message["role"] == "user" else "assistant",
                "content": [
                    {"type": "image_url", "image_url": {"url": message["image"], "detail": "high"}}
                ],
            }

            if "message" in message:
                image_message["content"].append({"type": "text", "text": message["message"]})

            if message["role"] == "assistant" and message == messages[-1]:
                image_message["content"].append(
                    {
                        "type": "text",
                        "text": "This is the result. Does that look right? Could it be closer to what we're aiming for, or is it done? Be detailed in exactly how we could improve it first, then write code to improve it. Unless you think it's done (I might agree)!",
                    }
                )

            new_messages.append(image_message)

            if "output" in message and message == messages[-1]:
                # Display the message if it's the placeholder warning
                if "placeholder" in message["output"].lower() or "traceback" in message["output"].lower():
                    if "text" in new_messages[-1]["content"][0]:
                        new_messages[-1]["content"][0]["text"] += (
                                "\n\nAlso, I received this output from the Open Interpreter code execution system we're using, which executes your markdown code blocks automatically: "
                                + message["output"]
                        )

    if not function_calling:
        new_messages = [msg for msg in new_messages if "content" in msg and len(msg["content"]) != 0]

    return new_messages
