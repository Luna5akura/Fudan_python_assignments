from rembg import remove


def remove_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as f_in:
        img_data = f_in.read()
    img_without_bg = remove(img_data)
    with open(output_image_path, "wb") as f_out:
        f_out.write(img_without_bg)


input_path = "./06_05__before_reisen.png"
output_path = "./06_05__after_reisen.png"
remove_background(input_path, output_path)
