Again, you can just solve this with a one line bash command.

```bash
cat rosalind_revc.txt  | rev | tr 'ATCG' 'TAGC'  > output.txt
```

