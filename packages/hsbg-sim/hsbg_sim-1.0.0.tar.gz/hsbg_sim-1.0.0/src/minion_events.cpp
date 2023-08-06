#include "battle.hpp"

// -----------------------------------------------------------------------------
// Aura buffs
// -----------------------------------------------------------------------------

bool Minion::recompute_aura_from(Board& board, int pos, Board const* enemy_board) {
  switch (type) {
    case MinionType::DireWolfAlpha:
      board.aura_buff_adjacent(double_if_golden(1), 0, pos);
      return true;
    case MinionType::MurlocWarleader:
      board.aura_buff_others_if(double_if_golden(2), 0, pos, [](Minion const& to){ return to.has_tribe(Tribe::Murloc); });
      return true;
    case MinionType::OldMurkEye: {
      // count murlocs for both players
      int count = pos >= 0 ? -1 : 0; // exclude self
      count += board.minions.count_if([](Minion const& to) { return to.has_tribe(Tribe::Murloc); });
      if (enemy_board) {
        count += enemy_board->minions.count_if([](Minion const& to) { return to.has_tribe(Tribe::Murloc); });
      }
      aura_buff(double_if_golden(count),0);
      return true;
    }
    case MinionType::PhalanxCommander:
      board.aura_buff_others_if(double_if_golden(2), 0, pos, [](Minion const& to){ return to.taunt; });
      return true;
    case MinionType::Siegebreaker:
      board.aura_buff_others_if(double_if_golden(1), 0, pos, [](Minion const& to){ return to.has_tribe(Tribe::Demon); });
      return true;
    case MinionType::MalGanis:
      board.aura_buff_others_if(double_if_golden(2), double_if_golden(2), pos,
        [](Minion const& to){ return to.has_tribe(Tribe::Demon); });
      return true;
    case MinionType::SouthseaCaptain:
      board.aura_buff_others_if(double_if_golden(1), double_if_golden(1), pos, [](Minion const& to){ return to.has_tribe(Tribe::Pirate); });
      return true;
    default:;
      return false;
  }
}

// -----------------------------------------------------------------------------
// Deathrattles
// -----------------------------------------------------------------------------

#define TWICE_IF_GOLDEN() for(int i=0;i<(golden?2:1);++i)

void Minion::do_deathrattle(Battle& battle, int player, int pos) const {
  switch (type) {
    // Tier 1
    case MinionType::Mecharoo:
      battle.summon(Minion(MinionType::JoEBot,golden), player, pos);
      break;
    case MinionType::SelflessHero:
      TWICE_IF_GOLDEN() {
        battle.board[player].give_random_minion_divine_shield(battle.rng, player);
      }
      break;
    case MinionType::FiendishServant:
      TWICE_IF_GOLDEN() {
        battle.board[player].buff_random_minion(this->attack,0, battle.rng, player);
      }
      break;
    case MinionType::Scallywag:
      battle.summon(Minion(MinionType::SkyPirate, golden), player, pos);
      // it attacks immediately
      battle.single_attack_by(player, pos);
      break;
    // Tier 2
    case MinionType::HarvestGolem:
      battle.summon(Minion(MinionType::DamagedGolem,golden), player, pos);
      break;
    case MinionType::KaboomBot:
      TWICE_IF_GOLDEN() {
        battle.damage_random_minion(1-player, 4);
      }
      // don't need to call check_for_deaths();
      break;
    case MinionType::KindlyGrandmother:
      battle.summon(Minion(MinionType::BigBadWolf,golden), player, pos);
      break;
    case MinionType::MountedRaptor:
      TWICE_IF_GOLDEN() {
        battle.summon(random_one_cost_minion(battle.rng, player), player, pos);
      }
      break;
    case MinionType::RatPack:
      battle.summon_many(attack, Minion(MinionType::Rat,golden), player, pos);
      break;
    case MinionType::SpawnOfNZoth:
      battle.board[player].buff_all(double_if_golden(1), double_if_golden(1));
      break;
    case MinionType::Imprisoner:
      battle.summon(Minion(MinionType::Imp,golden), player, pos);
      break;
    case MinionType::UnstableGhoul: {
      // Deal 1 damage to all minions
      battle.damage_all(0, 1);
      battle.damage_all(1, 1);
      break;
    }
    // Tier 3
    case MinionType::InfestedWolf:
      battle.summon_many(2, Minion(MinionType::Spider,golden), player, pos);
      break;
    case MinionType::PilotedShredder:
      TWICE_IF_GOLDEN() {
        battle.summon(random_two_cost_minion(battle.rng, player), player, pos);
      }
      break;
    case MinionType::ReplicatingMenace:
      battle.summon_many(3, Minion(MinionType::Microbot,golden), player, pos);
      break;
    case MinionType::TortollanShellraiser: {
      int amount = double_if_golden(1);
      battle.board[player].buff_random_minion(amount,amount,battle.rng,player);
      break;
    }
    // Tier 4
    case MinionType::PilotedSkyGolem:
      TWICE_IF_GOLDEN() {
        battle.summon(random_four_cost_minion(battle.rng, player), player, pos);
      }
      break;
    case MinionType::RingMatron: {
      battle.summon(Minion(MinionType::Imp, golden), player, pos);
      battle.summon(Minion(MinionType::Imp, golden), player, pos);
      break;
    }
    case MinionType::TheBeast:
      battle.summon_for_opponent(MinionType::FinkleEinhorn, player);
      break;
    // Tier 5
    case MinionType::GoldrinnTheGreatWolf: {
      int amount = double_if_golden(4);
      battle.board[player].buff_all_if(amount, amount, [](Minion const& x){return x.has_tribe(Tribe::Beast);});
      break;
    }
    case MinionType::KingBagurgle: {
      int amount = double_if_golden(2);
      battle.board[player].buff_all_if(amount, amount, [](Minion const& x){return x.has_tribe(Tribe::Murloc);});
      break;
    }
    case MinionType::MechanoEgg:
      battle.summon(Minion(MinionType::Robosaur,golden), player, pos);
      break;
    case MinionType::SatedThreshadon:
      battle.summon_many(3, Minion(MinionType::MurlocScout,golden), player, pos);
      break;
    case MinionType::SavannahHighmane:
      battle.summon_many(2, Minion(MinionType::Hyena,golden), player, pos);
      break;
    // Tier 6
    case MinionType::Ghastcoiler:
      for (int i=0; i<double_if_golden(2); ++i) {
        battle.summon(random_deathrattle_minion(battle.rng, player), player, pos);
      }
      break;
    case MinionType::KangorsApprentice:
      for (int i=0; i<double_if_golden(2) && battle.mechs_that_died[player].contains(i); ++i) {
        battle.summon(battle.mechs_that_died[player][i].new_copy(), player, pos);
      }
      break;
    case MinionType::SneedsOldShredder:
      TWICE_IF_GOLDEN() {
        battle.summon(random_legendary_minion(battle.rng, player), player, pos);
      }
      break;
    case MinionType::Voidlord:
      battle.summon_many(3, Minion(MinionType::Voidwalker,golden), player, pos);
      break;
    default:;
  }
  // extra deathrattles
  battle.summon_many(deathrattle_murlocs, MinionType::MurlocScout, player, pos);
  battle.summon_many(deathrattle_microbots, MinionType::Microbot, player, pos);
  battle.summon_many(deathrattle_golden_microbots, Minion(MinionType::Microbot,true), player, pos);
  battle.summon_many(deathrattle_plants, MinionType::Plant, player, pos);
}

// -----------------------------------------------------------------------------
// Events
// -----------------------------------------------------------------------------

void Minion::on_friendly_summon(Board& board, Minion& summoned, bool played) {
  switch (type) {
    case MinionType::MurlocTidecaller:
      if (summoned.has_tribe(Tribe::Murloc)) {
        buff(double_if_golden(1), 0);
      }
      break;
    case MinionType::WrathWeaver:
      if (played) {
        if (summoned.has_tribe(Tribe::Demon)) {
          // TODO: damage hero
          buff(double_if_golden(2), double_if_golden(2));
        }
      }
      break;
    case MinionType::CobaltGuardian:
      if (summoned.has_tribe(Tribe::Mech)) {
        divine_shield = true;
      }
      break;
    case MinionType::CrowdFavorite:
      if (played) {
        if (summoned.info().battlecry) {
          buff(double_if_golden(1), double_if_golden(1));
        }
      }
      break;
    case MinionType::PackLeader:
      if (summoned.has_tribe(Tribe::Beast)) {
        summoned.buff(double_if_golden(3), 0);
      }
      break;
    case MinionType::MamaBear:
      if (summoned.has_tribe(Tribe::Beast)) {
        summoned.buff(double_if_golden(4), double_if_golden(4));
      }
      break;
    case MinionType::PreNerfMamaBear:
      if (summoned.has_tribe(Tribe::Beast)) {
        summoned.buff(double_if_golden(5), double_if_golden(5));
      }
      break;
    case MinionType::DeflectOBot: {
      if (summoned.has_tribe(Tribe::Mech)) {
        buff(double_if_golden(1), 0);
        divine_shield = true;
      }
      break;
    }
    default:;
  }
}

void Minion::on_friendly_death(Battle& battle, Minion const& dead_minion, int player) {
  switch (type) {
    case MinionType::ScavengingHyena:
      if (dead_minion.has_tribe(Tribe::Beast)) {
        buff(double_if_golden(2), double_if_golden(1));
      }
      break;
    case MinionType::SoulJuggler:
      if (dead_minion.has_tribe(Tribe::Demon)) {
        TWICE_IF_GOLDEN() {
          battle.damage_random_minion(1-player, 3);
        }
        // already in a loop that does check_for_deaths();
      }
      break;
    case MinionType::Junkbot:
      if (dead_minion.has_tribe(Tribe::Mech)) {
        buff(double_if_golden(2), double_if_golden(2));
      }
      break;
    default:;
  }
}

void Minion::on_damaged(Battle& battle, int player, int pos) {
  switch (type) {
    case MinionType::ImpGangBoss:
      // Note: summons to the right
      battle.summon(Minion(MinionType::Imp,golden), player, pos+1);
      break;
    case MinionType::SecurityRover:
      battle.summon(Minion(MinionType::GuardBot,golden), player, pos+1);
      break;
    case MinionType::YoHoOgre: {
      if (health <= 0) break;
      // Survived being attacked, so it will attack immediately.
      battle.single_attack_by(player, pos);
      break;
    }
    case MinionType::TormentedRitualist: {
      // Whenever this is attacked, give adjacent minions +1/+1.
      battle.board[player].aura_buff_adjacent(double_if_golden(1), double_if_golden(1), pos);
      break;
    }
    default:;
  }

  // Qiraji Harbringer implementation
  int has_qiraji_harbringer = battle.board[player].has_minion(MinionType::QirajiHarbinger);
  if (type != MinionType::QirajiHarbinger && taunt && health <= 0 && has_qiraji_harbringer) {
    int buff = has_qiraji_harbringer == 2 ? 4 : 2;
    battle.board[player].aura_buff_adjacent(buff, buff, pos);
  }
}

void Minion::on_after_attack(Battle& battle, int player) {
  switch(type) {
    case MinionType::MonstrousMacaw: {
      int i = battle.board[player].random_minion_satisfying(
        [](Minion const& m){ return !m.dead() && m.info().deathrattle; },
        battle.rng, rng_key(RNGType::DeathrattleMinion, player)
      );
      if (i != -1) {
        battle.board[player].minions[i].do_deathrattle(battle, player, i);
      }
      break;
    }
    default:;
  }

  // Ripsnarl Captain implementation
  // Effect: whenever another friendly Pirate attacks, give it +2/+2.
  int has_ripsnarl_captain = battle.board[player].has_minion(MinionType::RipsnarlCaptain);
  if (type != MinionType::RipsnarlCaptain && has_tribe(Tribe::Pirate) && has_ripsnarl_captain) {
    int buff_amount = has_ripsnarl_captain == 2 ? 4 : 2;
    buff(buff_amount, buff_amount);
  }
}

void Minion::on_attack_and_kill(Battle& battle, int player, int pos, bool overkill) {
  switch (type) {
    case MinionType::IronhideDirehorn:
      if (overkill) {
        battle.summon(Minion(MinionType::IronhideRunt, golden), player, pos+1);
      }
      break;
    case MinionType::TheBoogeymonster:
      buff(double_if_golden(2),double_if_golden(2));
      break;
    case MinionType::HeraldOfFlame: {
      if (!overkill) break;
      int enemy_player = 1-player;
      auto& minions = battle.board[enemy_player].minions;
      for (int i = 0; i < minions.size(); ++i) {
        if (minions[i].alive() && minions[i].exists()) {
          battle.damage(enemy_player, i, 3);
          break;
        }
      }
      break;
    }
    default:;
  }

  // Waxrider Togwaggle implementation
  // Effect: Whenever a friendly minion Dragon kills an enemy, gain +2/+2.
  int has_waxrider_togwaggle = battle.board[player].has_minion(MinionType::WaxriderTogwaggle);
  if (type != MinionType::WaxriderTogwaggle && has_tribe(Tribe::Dragon) && has_waxrider_togwaggle) {
    auto& minions = battle.board[player].minions;
    for (int i = 0; i < minions.size(); ++i) {
      if (minions[i].type == MinionType::WaxriderTogwaggle) {
        int buff = has_waxrider_togwaggle == 2 ? 4 : 2;
        minions[i].buff(buff, buff);
      }
    }
  }
}

void Minion::on_after_friendly_attack(Minion const& attacker) {
  switch (type) {
    case MinionType::FesterootHulk:
      buff(double_if_golden(1),0);
      break;
    case MinionType::GlyphGuardian:
      if (attacker.type == MinionType::GlyphGuardian) {
        int multiplier = golden ? 2 : 1;
        buff(attack * multiplier, 0);
      }
      break;
    default:;
  }
}

void Minion::on_break_friendly_divine_shield() {
  switch (type) {
    case MinionType::BolvarFireblood:
      buff(double_if_golden(2),0);
      break;
    case MinionType::DrakonidEnforcer: {
      buff(double_if_golden(2), double_if_golden(2));
      break;
    }
    default:;
  }
}

// -----------------------------------------------------------------------------
// Battlecries
// -----------------------------------------------------------------------------

Tribe Minion::battlecry_target() const {
  switch (type) {
    case MinionType::RockpoolHunter:
      return Tribe::Murloc;
    case MinionType::NathrezimOverseer:
      return Tribe::Demon;
    case MinionType::Houndmaster:
      return Tribe::Beast;
    case MinionType::Toxfin:
      return Tribe::Murloc;
    case MinionType::VirmenSensei:
      return Tribe::Beast;
    default:
      return Tribe::None;
  }
}

