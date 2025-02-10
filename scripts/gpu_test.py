import torch


def gpu_test():
    if not torch.cuda.is_available():
        print("CUDA is not available. Running on CPU.")
        device = torch.device("cpu")
    else:
        device = torch.device("cuda")
        print(f"CUDA is available! Running on {torch.cuda.get_device_name(0)}.")

    # Create a small tensor and move it to GPU (if available)
    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = torch.tensor([4.0, 5.0, 6.0], device=device)

    # Perform a simple computation
    z = x + y
    print("Tensor computation result:", z)


if __name__ == "__main__":
    gpu_test()
