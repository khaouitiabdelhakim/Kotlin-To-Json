f = open("QuranFrench.kt", "r", encoding="utf-8")
g = open("QuranFrench.js", "w", encoding="utf-8")

i = 0

g.write("""/**
 * This class provides access to the Holy Quran French Translation data.
 * For copyright and usage information, refer to the author's GitHub repository.
 * Last modification: 18th March 2024
 * Quote: "Anyone can use this library. Don't forget to pray for us, and may Allah forgive our sins."
 * Source: https://surahquran.com
 *
 * @author ABDELHAKIM KHAOUITI
 * @github khaouitiabdelhakim
 */\n\n\n""")

g.write("const QuranFrench = [\n")

for line in f:
    if i < 5:  # Skip the first 5 lines
        i += 1
        continue

    if "arrayOf(" in line:
        g.write("[\n")
    elif ")," in line and len(line) <= 12:
        g.write("],\n")
    elif ")" in line and len(line) <= 12:
        g.write("]\n")
    else:
        if "}" not in line:
            line = line.replace('"', '\"')  # Escape double quotes
            g.write(line)

g.write("\n\n\nmodule.exports = QuranFrench;")

f.close()
g.close()
