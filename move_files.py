# https://pythonhelp.ru/python/kak-peremestit-fail-iz-odnoi-papki-v-druguiu-python/

import shutil, os

# Укажите полный путь к файлу, который вы хотите переместить
src = 'COCO' # 123402 images

# Укажите полный путь к папке, в которую вы хотите переместить файл
dst1 = 'cover6' # 123402/2 = 61701 images

# Используйте функцию shutil.move() для перемещения файла
for i, filename in enumerate(os.listdir(src)):
	if i == 61701:
		break
	else:
		shutil.move(src + "/" + filename, dst1 + "/" + filename)
		i += 1

dst2 = 'wm6' # 123402/2 = 61701 images

for i, filename in enumerate(os.listdir(src)):
	shutil.move(src + "/" + filename, dst2 + "/" + filename)