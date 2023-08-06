# Parametric SVG Utility

`psvg-cli` is a commandline utility for applying various transformations to Parametric SVG files.

It is written in Python, using the [click](https://click.palletsprojects.com) library for commandline interfaces, and follows the same pattern as the [imagepipe example](https://github.com/pallets/click/blob/master/examples/imagepipe/imagepipe.py) for [multi-command chaining](https://click.palletsprojects.com/en/7.x/commands/#multi-command-chaining).

You can access help for the tool as a whole (`psvg-cli --help`), or for a specific command (`psvg-cli process --help`), or a subcommand (`psvg-cli process open --help`).


## Examples

```
psvg-cli parameters glyph_definitions/*

psvg-cli process opendir ./glyph_definitions -i glyph_definitions/CDS.svg remove_parametric_params save

psvg-cli process open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params save
psvg-cli process open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params save --format all
psvg-cli process open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params delete_by_class -c baseline save 
psvg-cli process open -i glyph_definitions/Aptamer.svg apply_transformation save 

psvg-cli process \
open -i glyph_definitions/Aptamer.svg \
style_class -c "baseline" -s "opacity:1;fill:none;fill-opacity:1;stroke:#b3b3b3;stroke-width:0.49999994; stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:1,0.5; stroke-dashoffset:0;stroke-opacity:1" \
save

psvg-cli process \
open -i glyph_definitions/Aptamer.svg \
substitute -o width -n w \
save

```

By default, the results of `process` commands will be written to a `./processed` directory.
