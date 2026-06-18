# Push Notification Sources

All sources that can send push notifications to your iPhone via the Claude mobile app.

## Interactive Sessions

| Source | Trigger | Description |
|--------|---------|-------------|
| Ad-hoc session | On demand | Any Claude Code session (web or Remote Control) can send a push notification when asked, or when a long task finishes. |

## Routines

> To add push notifications to a routine, append this line to its prompt at [claude.ai/code/routines](https://claude.ai/code/routines):
> ```
> When you finish, send me a push notification summarizing what was done.
> ```

| Routine | Schedule | Description |
|---------|----------|-------------|
| _(none configured yet)_ | — | Add your routines here as you enable notifications for them. |

## Agents

| Agent | Project | Description |
|-------|---------|-------------|
| _(none configured yet)_ | — | Add background agents here as you set them up. |

## Settings

Push notifications are globally enabled in `~/.claude/launcher-settings.json`:

- `agentPushNotifEnabled: true` — allows Claude to push proactive notifications
- `inputNeededNotifEnabled: true` — pushes when Claude needs your input
- `PushNotification` in `permissions.allow` — no permission prompt required

## Managing Notifications

- **Disable globally**: set `agentPushNotifEnabled: false` in `~/.claude/launcher-settings.json`
- **Disable for a routine**: remove the push notification instruction from the routine's prompt
- **iOS settings**: Settings → Notifications → Claude
