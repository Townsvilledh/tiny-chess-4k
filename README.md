# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Townsvilledh/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Townsvilledh/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,081 bytes of Python, built for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty ($500 in USDC). 0x88 board, alpha-beta search with quiescence, six piece-square tables, MVV-LVA move ordering, and a fixed 50,000-node budget per move (`CHESS_NODES`) — deterministic, standard library only, never a clock.

## Run it

The engine plays through the make.fun environment server:

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18081 python3 main.py
```

## The size rule

- `main.py` is the whole engine: at most 4,096 bytes as committed, Python 3.13, standard library only. It reads, imports or execs no other file in the repository.
- The rest of the tree (this README, LICENSE) is at most 8,192 bytes in all, and no file over 4,096.
- Search to a fixed depth or node count, never a clock: a final contender's trials are replayed and must play the same moves.

---

<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
