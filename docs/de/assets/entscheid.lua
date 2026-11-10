-- Quarto filter for docs/de (registered in docs/de/_metadata.yml): shows the
-- excerpt of the data model above the text of a modelling decision.
--
--   ::: {.entscheid}
--   ![](assets/excerpts/name.svg){fig-alt="Description of the excerpt"}
--
--   Text of the decision ...
--   :::
--
-- The excerpt keeps its natural size, so that the labels of small excerpts
-- are not enlarged and those of large excerpts stay readable; the width is
-- read from the SVG file and limited to the width of the text. The text uses
-- the full width of the page below the excerpt.
--
--   * HTML: width as inline style, spacing in entscheid.css (added as HTML
--     dependency);
--   * Typst (PDF): width in pt;
--   * other formats (Markdown, Word): unchanged.

-- Width of the text in the PDF (A4 minus 2 cm and 1.5 cm margin).
local PDF_TEXT_WIDTH_PT = 496

-- Width of an SVG file in pixels (PlantUML writes "width:123px" into the
-- style of the root element), or nil.
local function svg_width(src)
  local path = pandoc.path.join({ pandoc.path.directory(quarto.doc.input_file), src })
  local file = io.open(path, "r")
  if not file then return nil end
  local head = file:read(2000) or ""
  file:close()
  local width = head:match("width:(%d+)px") or head:match('width="(%d+)')
  return width and tonumber(width) or nil
end

local function size_image(img)
  local px = svg_width(img.src)
  if not px then return nil end
  if quarto.doc.is_format("html") then
    img.attributes["style"] = string.format("width: %dpx;", px)
  elseif quarto.doc.is_format("typst") then
    img.attributes["width"] = string.format("%.0fpt", math.min(px * 0.75, PDF_TEXT_WIDTH_PT))
  end
  return img
end

function Div(div)
  if not div.classes:includes("entscheid") then return nil end
  if quarto.doc.is_format("html") then
    quarto.doc.add_html_dependency({
      name = "entscheid", version = "2.0", stylesheets = { "entscheid.css" },
    })
  end
  return div:walk({ Image = size_image })
end
