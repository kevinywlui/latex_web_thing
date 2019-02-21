# Latex Web Thing
- A project by Nikolas Eptaminitakis, Kevin Lui, and Gerardo Zelaya
- Use https://mathscinet.ams.org/mrlookup to automatically fill in your
citations

## TODO:

- [ ] Use the user's citation-key as the bibtex citation-key. For example, the
  bibtex entry generated by `\cite{mazur:eisenstein}` should yield `@article
  {mazur:eisenstein ...`
- [ ] Handle multiple or no entries on mrlookup. Prompt user at the end.
- [ ] Handle optional arguments in citation: `\cite[Prop
  14.2]{mazur:eisenstein}` but maybe we don't actually have to do this since
  the aux file might have stripped this out.
- [ ] Perhap send multiple requests? But this might make amsmath mad.
- [ ] Handle no/poor network connection.
- [ ] See if there's a better way to integrate into pdflatex than what's
  already being down. Is there a way to integrate into latexmk?
- [ ] See if there's a way to have multiple bibtex citation-key to a single
  entry. If so, how should we handle this?
