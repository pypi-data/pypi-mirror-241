# DBnomics PowerPoint (pptx) tools

This CLI tool allows to update data coming from DBnomics in PowerPoint presentations.

## Example

See the [samples directory](https://git.nomics.world/dbnomics/dbnomics-pptx-tools/-/tree/main/samples)

## Usage

First, define a YAML metadata file describing the charts and tables on each slide to update.

Read the [metadata file](#metadata-file) section below for more details.

Take inspiration from the sample [simple_presentation_1.yaml](https://git.nomics.world/dbnomics/dbnomics-pptx-tools/-/blob/main/samples/simple_presentation_1.yaml)

### `fetch` command

This command reads all the series needed by the charts and tables of all slides in the YAML metadata file, deduplicate and download them in a cache directory, where they are stored as JSON files.

```bash
dbnomics-pptx fetch samples/simple_presentation_1.yaml
```

Use the `-v` option to display debug messages.

By default, the series that always downloaded, even if they are already present in the cache directory.
Use the `--resume` option otherwise.

### `save-data-archive` command

This command creates a ZIP archive of the series used to update the presentation (cf `update` command).

```bash
dbnomics-pptx -v save-data-archive samples/simple_presentation_1.yaml series.zip
unzip -t series.zip
    Archive:  series.zip
        testing: OECD/KEI/NAEXKP01.DEU.GP.A.csv   OK
        testing: OECD/GDP_GROWTH/W.Eurozone.tracker_yoy.csv   OK
        testing: OECD/KEI/NAEXKP01.EA20.GP.A.csv   OK
        testing: OECD/KEI/NAEXKP01.FRA.GP.A.csv   OK
        testing: OECD/GDP_GROWTH/W.USA.tracker_yoy.csv   OK
        testing: OECD/KEI/NAEXKP01.ITA.GP.A.csv   OK
    No errors detected in compressed data of series.zip.
```

### `update` command

This command takes a PowerPoint presentation file in input, and a YAML metadata file, and updates the charts and tables defined in the metadata file, then saves the result in an output presentation file (it does not modify the input one).

```bash
dbnomics-pptx update samples/simple_presentation_1.pptx --metadata-file samples/simple_presentation_1.yaml samples/simple_presentation_1.output.pptx
```

Use the `-v` option to display debug messages.

## Metadata file

Here is a dummy file with made-up IDs to show how it is structured:

```yaml
slides:
  AE_GDP: # the ID of the slide (as defined in the slide notes, cf below)
    charts:
      US_EU_GDP: # the ID of the chart (as defined in the "Selection pane")
        series:
          - id: OECD/GDP_GROWTH/W.USA.tracker_yoy # the ID of the series on DBnomics
            name: United States
          - id: OECD/GDP_GROWTH/W.Eurozone.tracker_yoy
            name: Eurozone
    tables:
      EU_GDP: # the ID of the table (as defined in the "Selection pane")
        series:
          - id: OECD/KEI/NAEXKP01.EA19.GP.A
            name: Euro Area
          - id: OECD/KEI/NAEXKP01.DEU.GP.A
            name: Germany
          - id: OECD/KEI/NAEXKP01.FRA.GP.A
            name: France
          - id: OECD/KEI/NAEXKP01.ITA.GP.A
            name: Italy
```

### Slide ID

To be updated, a slide must have been given an ID. As PowerPoint does not provide a way to assign one, we decided to use a special string in the slide notes, by using the syntax `slide_id:xxx` where `xxx` is to be replaced with the real value. For example, in the YAML file above, the slide ID is `AE_GDP`, so we expect the corresponding slide notes to contain the string `slide_id:AE_GDP`.

### Chart and table ID

The IDs of the charts and tables can be read or modified from the "Selection pane" in PowerPoint.

The "Selection pane" can be opened with Alt+F10 in PowerPoint.
Then you just have to select a chart or a table, and it will highlight the corresponding line in the "Selection pane", showing its ID.

You can also modify the ID to improve readability.

Once you get the ID of a chart or a table, you can put it in the YAML file.
In the previous example, the IDs are "My chart 1" and "My table 1".

See also:

- [Manage objects with the Selection pane](https://support.microsoft.com/en-us/office/manage-objects-with-the-selection-pane-a6b2fd3e-d769-46c1-9b9c-b94e04a72550)
- [The PowerPoint Selection Pane](https://www.presentationpoint.com/blog/powerpoint-selection-pane/)
