import torch
import argparse
from train import BiagramLanguageModel
from text_utils import encode, decode
from scripts.text_utils import vocab_size

def generate_text(model, start_text, max_new_tokens, block_size, device):
    encoded_input = torch.tensor(encode(start_text), dtype=torch.long).unsqueeze(0).to(device)
    generated_ids = model.generate(encoded_input, max_new_tokens)
    return decode(generated_ids[0].tolist())

def main():
    parser = argparse.ArgumentParser(description="Generate text from a starting string using a trained model.")
    parser.add_argument('start_text', type=str, help="Starting text for the generation. Must be in quote marks!")
    parser.add_argument('max_new_tokens', type=int, help="Maximum number of new tokens to generate")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_path = 'model.pth'
    start_text = args.start_text
    max_new_tokens = args.max_new_tokens
    block_size = 256

    model = BiagramLanguageModel(vocab_size).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    generated_text = generate_text(model, start_text, max_new_tokens, block_size, device)
    
    print(generated_text)

if __name__ == "__main__":
    main()
