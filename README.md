# Portfólio — Eliane Souza Ferreira · Síndica Profissional

Material de apresentação **comercial premium** (não um currículo simples) para a atuação da Eliane
como Síndica Profissional, com foco em design, credibilidade, organização visual e impacto comercial.

> **Entregável final:** [`portfolio_eliane_sindica_profissional.pdf`](portfolio_eliane_sindica_profissional.pdf) — 12 páginas, A4, pronto para apresentação.

---

## 📄 O que é

PDF de 12 páginas gerado a partir de **HTML/CSS** (renderizado com Playwright/Chromium). Estrutura:

1. **Capa** — nome, título e subtítulo sobre foto institucional
2. **Apresentação** — texto institucional + painel de números
3. **Experiência em gestão condominial** — Parque Amarige, Shopping do Carmo, Ulisses dos Santos Ribeiro
4. **Trajetória profissional** — linha do tempo (currículo antigo)
5. **Formação, cursos e capacitações** — SINDICONET (2021), SEBRAE (2017), Café com Síndico (2022)
6–7. **Obras e melhorias — Parque Amarige** — antes/depois + obra em andamento + vitrine
8–9. **Obras e melhorias — Ipê Roxo** — piscina (frames de vídeo), espaço gourmet, jardim + vitrine
10. **Outras frentes de atuação** — 8 cards (gestão, finanças, obras, moradores, assembleias, fornecedores…)
11. **Diferenciais profissionais**
12. **Encerramento** — frase de impacto + contatos

---

## 🗂 Estrutura do repositório

```
.
├── portfolio_eliane_sindica_profissional.pdf   ← ENTREGÁVEL FINAL (cópia na raiz)
├── eliane_curriculo-1 7 (1).pdf                 ← fonte: currículo antigo
├── 80a99a16-...jpg                              ← fonte: imagem dos cursos
├── Condominios antes e depois/                  ← fonte: fotos e vídeos
│   ├── Parque Amarige/{antes,depois}/
│   └── IPE Roxo/{antes,depois}/   (3 vídeos .mp4)
├── output/
│   ├── portfolio.html               ← código-fonte do portfólio (HTML/CSS)
│   ├── gen_pdf.py                   ← gera o PDF (e copia p/ a raiz)
│   ├── portfolio_eliane_sindica_profissional.pdf
│   ├── assets/                      ← imagens otimizadas + fontes (.woff2) + fonts.css
│   └── generated_frames/            ← melhores frames extraídos dos vídeos
├── README.md
└── CLAUDE.md                         ← guia para futuras sessões do Claude Code
```

---

## 🔄 Como regenerar o PDF

Depois de editar `output/portfolio.html` (ou trocar imagens em `output/assets/`):

```powershell
cd output
python gen_pdf.py            # gera o PDF e copia automaticamente para a raiz
python gen_pdf.py --shots    # idem + screenshots por página em output/_shots/ (revisão)
```

### Dependências (uma vez)
```powershell
pip install playwright pillow pymupdf imageio imageio-ffmpeg numpy
python -m playwright install chromium
```
As fontes (Cormorant Garamond + Montserrat) já estão **embutidas** em `output/assets/fonts/` — não precisa de internet para regenerar.

---

## 🎨 Identidade visual

| Elemento | Valor |
|---|---|
| Off-white (fundo) | `#F6F3ED` |
| Grafite (texto) | `#23282E` |
| Azul petróleo (institucional) | `#11414A` / `#0B2B31` |
| Dourado discreto (destaque) | `#B08A4E` / `#C7A56B` |
| Tipografia display | Cormorant Garamond (serifada) |
| Tipografia texto/rótulos | Montserrat |

---

## ⚠️ Conteúdo e privacidade

- Conteúdo em **português do Brasil**; textos do currículo foram revisados e tornados institucionais (sem inventar fatos).
- **Não inventar** dados pessoais/profissionais — usar apenas os arquivos-fonte + dados confirmados (ver `CLAUDE.md`).
- Imagens com **placas de veículos / rostos de terceiros** foram evitadas, recortadas ou mantidas apenas quando ilegíveis/não identificáveis.
- Fotos antes/depois existem **apenas** para Parque Amarige e Ipê Roxo; os demais trabalhos aparecem de forma textual.

Detalhes completos de dados, decisões e convenções em **[`CLAUDE.md`](CLAUDE.md)**.
