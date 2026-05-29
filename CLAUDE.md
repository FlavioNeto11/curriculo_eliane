# CLAUDE.md — Guia do projeto para o Claude Code

Contexto e convenções para futuras sessões. **Leia antes de editar.**

## 🎯 Objetivo
Manter/evoluir um **portfólio comercial premium** (PDF) da **Eliane Souza Ferreira**, posicionada como
**Síndica Profissional**. É material de apresentação executiva — **não** um currículo Word/simples.

- **Entregável:** `portfolio_eliane_sindica_profissional.pdf` na raiz (cópia em `output/`).
- **Fonte de verdade do layout:** `output/portfolio.html` (HTML + CSS inline, 12 `<section class="page">` = 12 páginas A4).
- **Idioma:** português do Brasil. Usar sempre **"Síndica Profissional"** e **"Portfólio"** com acento.

## 🔄 Fluxo de trabalho (sempre)
1. Edite `output/portfolio.html` e/ou imagens em `output/assets/`.
2. Regenere: `cd output && python gen_pdf.py` (gera o PDF **e copia para a raiz** automaticamente).
3. Para revisar visualmente: `python gen_pdf.py --shots` → PNGs em `output/_shots/` (ignorado pelo git) → abra/Read os PNGs.
4. Itere até ficar bom. Confira que cada página A4 **não corta** títulos, cards ou fotos.

Ambiente: **Windows**, Python 3.12, shell PowerShell. PDF via **Playwright/Chromium** (`print_background=True`, A4).
ffmpeg vem do pacote **imageio-ffmpeg** (não há ffmpeg no sistema). numpy/Pillow/PyMuPDF disponíveis. **Sem OpenCV, sem WeasyPrint.**

## ✅ Dados confirmados (NÃO inventar nada além disto)
**Pessoa:** Eliane Souza Ferreira · Síndica Profissional
**Contato:** (16) 99738-2936 · lidossantossouza@gmail.com  *(único contato disponível; não há endereço/CNPJ/registro)*

**Condomínios em destaque (dados fornecidos pelo cliente — autoritativos):**
- **Parque Amarige** — síndica **desde 2017** (atuação atual). *(currículo dizia 2017–2023; usar "desde 2017")*
- **Shopping do Carmo** — **4 mandatos**. *(currículo dizia 2022–2023; enfatizar "4 mandatos")*
- **Ulisses dos Santos Ribeiro** — **10 anos** de atuação. *(NÃO consta no currículo antigo; sem datas/descrição específicas — manter genérico e profissional)*

**Trajetória do currículo antigo** (`eliane_curriculo-1 7 (1).pdf`, fiel): COCISA — Síndica (2000–2008);
Essencial Nutrição — Gerente Operacional Jr. (2006–2008); Grupo Stuchi — Aux. Administrativo (2008–2009);
Dabeana Serviços — Proprietária (2010–2016); Dabeana Nutrição — Proprietária (2013–2020).

**Cursos** (do currículo + imagem `80a99a16-...jpg`):
- **SINDICONET (2021):** Gestão Condominial; Legislação I, II e III; Implantação de Condomínio; Segurança em Condomínio; Gestão Financeira; Gestão de RH I e II; Sustentabilidade; Condomínio Clube; Manutenção Predial; Assembleia.
- **SEBRAE (2017):** Gestão Financeira; Planejamento Financeiro.
- **Café com Síndico (2022):** palestras com Dr. Rodrigo Karpat, Comgás (Ronaldo Andreos), Campseg/Auto Defesa Brasil, Administradora Puiatti (Guilherme Gomes), Superlógica (Dra. Elisângela Thomazini).

## 🖼 Imagens — origem e tratamento
- Fotos antes/depois: **apenas Parque Amarige e Ipê Roxo** (`Condominios antes e depois/.../{antes,depois}`).
- **Ipê Roxo tem 3 vídeos** (`.mp4`) — a piscina aparece **em obra (antes)** e **finalizada (depois)** só nos vídeos.
  Frames já extraídos/curados em `output/generated_frames/` e usados no PDF. Para reextrair: `fps=2` + score de nitidez
  (variância do Laplaciano via numpy) — ver histórico de como foi feito.
- Imagens otimizadas (EXIF corrigido, ≤1400px, JPEG q≈84) ficam em `output/assets/` com nomes descritivos
  (`pa_*` = Parque Amarige, `ipe_*` = Ipê Roxo; `_antes/_depois/_show_*`).

### Regras de privacidade (obrigatórias)
- **Placas de veículos e rostos de terceiros**: evitar, recortar (`background-position`) ou só usar se ilegíveis/não identificáveis.
- A **capa** foi recortada para remover carros; a **fachada "antes"** foi reposicionada pelo mesmo motivo.
- A foto de obra na fachada (operário em rapel) é OK: rosto não identificável.

## ✍️ Regras de conteúdo
- Não inventar fatos. Pode melhorar redação (tom institucional/comercial) e corrigir português.
- Trabalhos **sem foto** ainda devem aparecer de forma textual/diagramada (cards, timeline) — nunca lista crua.
- Legendas de obras: genéricas e elegantes quando o nome técnico não for claro (ex.: "Revitalização paisagística",
  "Pintura e conservação de fachada", "Readequação de espaço") — **sem inventar detalhes técnicos**.

## 📌 Pendências / decisões em aberto
- **Sem foto profissional (headshot)** da Eliane utilizável: a única no currículo é pequena/baixa resolução. Não usada.
  Se o cliente enviar uma foto boa, considerar inserir na capa e/ou na página de Apresentação.
- **Ulisses dos Santos Ribeiro**: falta descrição/datas reais — texto atual é genérico de propósito.
- Espaço para **mais contatos** (endereço, redes, registro) está reservado no encerramento, caso surjam.

## 🚫 Não versionar (já no `.gitignore`)
`_frames_raw/`, `_review/`, `output/_shots/`, `__pycache__/`, arquivos `_cv_*`, `_cursos_*`, `_pdfcheck_*`.
