import os
import urllib.request

fonts_dir = os.path.join('assets', 'fonts')
css_dir = os.path.join('assets', 'css')

# Ensure directories exist
os.makedirs(fonts_dir, exist_ok=True)
os.makedirs(css_dir, exist_ok=True)

# Define fonts to download (using specific weights for Bitter, Inter, Maitree)
fonts = [
    {
        'family': 'Bitter',
        'url': 'https://fonts.gstatic.com/s/bitter/v33/rax_HiqOu8IVPmn7enFOP9_MIpE.woff2', # 400
        'weight': 400,
        'filename': 'bitter-regular.woff2'
    },
    {
        'family': 'Bitter',
        'url': 'https://fonts.gstatic.com/s/bitter/v33/rax_HiqOu8IVPmn7enFOP-_MIpE.woff2', # 700
        'weight': 700,
        'filename': 'bitter-bold.woff2'
    },
    {
        'family': 'Inter',
        'url': 'https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZJhjp-Ek-_EeA.woff2', # 400
        'weight': 400,
        'filename': 'inter-regular.woff2'
    },
    {
        'family': 'Inter',
        'url': 'https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuG1fAZJhjp-Ek-_EeA.woff2', # 600
        'weight': 600,
        'filename': 'inter-semibold.woff2'
    },
    {
        'family': 'Maitree',
        'url': 'https://fonts.gstatic.com/s/maitree/v14/0O47OaWy-B4_J_t-8Fp6p0R2.woff2', # 400
        'weight': 400,
        'filename': 'maitree-regular.woff2'
    }
]

css_content = ""

for font in fonts:
    filepath = os.path.join(fonts_dir, font['filename'])
    try:
        urllib.request.urlretrieve(font['url'], filepath)
        print(f"Downloaded {font['filename']}")
        
        css_content += f"""@font-face {{
  font-family: '{font['family']}';
  font-style: normal;
  font-weight: {font['weight']};
  font-display: swap;
  src: url('../fonts/{font['filename']}') format('woff2');
}}
"""
    except Exception as e:
        print(f"Failed to download {font['filename']}: {e}")

# Write fonts.css
with open(os.path.join(css_dir, 'fonts.css'), 'w') as f:
    f.write(css_content)

print("fonts.css created successfully.")
