contents = ["I like geophysics",
            "Python coding is fun!",
            "I rewrote our processing software for my current job which will be commercial soon. It is in the beta phase."]

filenames = ['geophysics.txt',
             'codingIsFun.txt',
             'rewroteSoftware.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
