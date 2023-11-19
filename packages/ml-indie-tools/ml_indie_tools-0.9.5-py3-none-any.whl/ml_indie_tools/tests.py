# %%
%load_ext autoreload
%autoreload 2

# %%
import sys
sys.path.append('/Users/dsc/gith/domschl/ml-indie-tools/src/ml_indie_tools')  # Point to local module source

# %%
import logging
logging.basicConfig(encoding='utf-8', level=logging.INFO)
from Gutenberg_Dataset import Gutenberg_Dataset
from Text_Dataset import Text_Dataset

# %%
gd=Gutenberg_Dataset()
gd.load_index()
bl=gd.search({'title': ['proleg', 'hermen'], 'language': ['english']})
bl=gd.insert_book_texts(bl)
for i in range(len(bl)):
    print(bl[i]['title'])

# %%
tl = Text_Dataset(bl)  # bl contains a list of texts (books from Gutenberg)
tl.source_highlight("If we write anything that contains parts of the sources, like: that is their motto, then a highlight will be applied.")

# %%
test_text="That would be a valid argument if we hadn't defeated it's assumptions way before."
print(f"Text length {len(test_text)}, {test_text}")
tokenizer='bytegram'  # 'ngram'
tl.init_tokenizer(tokenizer=tokenizer)
st = tl.tokenize(test_text)
print(f"Token-count: {len(st)}, {st}")

# %%
test2="ðƒ "+test_text
print(f"Text length {len(test2)}, {test2}")
el=tl.encode(test2)
print(f"Token-count: {len(el)}, {el}")

# %%
tl.init_getitem("encoded")

# %%
tl.decode(tl[3])

# %%
tl.get_unique_token_count()

# %%



