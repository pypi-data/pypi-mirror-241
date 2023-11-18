import gdown
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Down load model from google drive")
    parser.add_argument(
        "--save_dir",
        "-p",
        required=True,
        type=str,
        help="model paths",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    url_links = {
        "encoder.onnx": "https://drive.usercontent.google.com/download?id=1hPJphUajDdbz7W47D2RvuDe2qImq7xgY&export=download&authuser=0&confirm=t&uuid=7f1e8b1f-b7c3-40f3-a384-acb83d6aad0f&at=APZUnTWCI39CPd98bWjrUqL9o_6Y:1698682706043",
        "decoder.onnx": "https://drive.usercontent.google.com/download?id=1BAUTUoebUBm0f0saILWGaV37pM-lwu-x&export=download&authuser=0&confirm=t&uuid=50372483-def7-4cce-a596-079d763eed54&at=APZUnTUUyRIKK6itjX-LLRBBo1Ul:1698682739555",
        "cnn.onnx": "https://drive.usercontent.google.com/download?id=1y7x9zofI1hFrjg3V3sktivIFuMP3uxoN&export=download&authuser=0&confirm=t&uuid=fda7fd53-6e2d-4948-8d3f-cfd75c2837e1&at=APZUnTXubx2NmK1D6Oq9fE-BTA5B:1698682775739",
    }

    model_dir = args.save_dir
    os.makedirs(model_dir, exist_ok=True)
    for model in url_links:
        path_model = os.path.join(model_dir, model)
        gdown.download(url_links[model], path_model, quiet=False)

    print("Model dirs: ", os.path.abspath(model_dir))


if __name__ == "__main__":
    main()
