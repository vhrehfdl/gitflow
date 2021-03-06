from models.base_model import BaseModel
from utils.evaluation import Evaluation


# def load_data(train_dir, test_dir):
#     tokenizer = get_tokenizer('basic_english')

#     text = data.Field(sequential=True, batch_first=True, lower=True, fix_length=50, tokenize=tokenizer)
#     label = data.LabelField()

#     train = TabularDataset(path=train_dir, skip_header=True, format='csv', fields=[('text', text), ('label', label)])
#     test = TabularDataset(path=test_dir, skip_header=True, format='csv', fields=[('text', text), ('label', label)])

#     train, valid = train.split(split_ratio=0.8)

#     return train, valid, test, text, label


# def pre_processing(train_data, valid_data, test_data, text, label, device, batch_size):
#     text.build_vocab(train_data)
#     label.build_vocab(train_data)

#     train_iter, val_iter = data.BucketIterator.splits((train_data, valid_data), batch_size=batch_size, device=device, sort_key=lambda x: len(x.text), sort_within_batch=False, repeat=False)
#     test_iter = data.Iterator(test_data, batch_size=batch_size, device=device, shuffle=False, sort=False, sort_within_batch=False)

#     return train_iter, val_iter, test_iter, text, label


# def train(model, optimizer, train_iter, device):
#     model.train()
#     for b, batch in enumerate(train_iter):
#         x, y = batch.text.to(device), batch.label.to(device)
#         optimizer.zero_grad()

#         logit = model(x)
#         loss = F.cross_entropy(logit, y)
#         loss.backward()
#         optimizer.step()

#     return model


def main():
    # Hyper parameter
    batch_size = 64
    lr = 0.001
    epochs = 3


    # Directory
    train_dir = "../data/binary_train.csv"
    test_dir = "../data/binary_test.csv"
    model_dir = "./model_save/text_classification.pt"

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    # print("1.Load data")
    # train_data, val_data, test_data, text, label = load_data(train_dir, test_dir)
    
    # print("2.Pre processing")
    # train_iter, val_iter, test_iter, text, label = pre_processing(train_data, val_data, test_data, text, label, device, batch_size)
    # batch = next(iter(train_iter)) # ????????? ????????????
    # print(batch.text)
    # print(batch.label)


    print("3.Build model")
    model = BaseModel(
        hidden_dim=32, 
        vocab_num = 200, 
        embedding_dim=300, 
        class_num=1).to(device)
    # optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    # print("4.Train")
    # best_val_loss = None
    # for e in range(1, epochs + 1):
    #     model = train(model, optimizer, train_iter, device)
    #     val_loss, val_accuracy = Evaluation(model, val_iter, device).eval_classification()
    #     print("[Epoch: %d] val loss : %5.2f | val accuracy : %5.2f" % (e, val_loss, val_accuracy))
    #     save_model(best_val_loss, val_loss, model, model_dir)

    # model.load_state_dict(torch.load(model_dir))
    # test_loss, test_acc = Evaluation(model, test_iter, device).eval_classification()
    # print('????????? ??????: %5.2f | ????????? ?????????: %5.2f' % (test_loss, test_acc))


if __name__ == '__main__':
    main()