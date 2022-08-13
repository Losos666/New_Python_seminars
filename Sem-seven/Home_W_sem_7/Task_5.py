from ast import Return


new_text = "напишите абв пинокабв поабв за...абв программу удаляющую изабв абв из этого текстаабв текста все абв слова которые содержат (страшная,трагичная-пустота) то что вы всеравно не увидите - поскольку я все удалил ахахахаха!!!!!"
def del_words(new_text):
    new_text = list(filter(lambda x: 'абв' not in x,new_text.split()))
    return " ".join(new_text)

new_text = del_words(new_text)
print(new_text)